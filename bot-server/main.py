from UnlimitedGPT import ChatGPT
from UnlimitedGPT.internal.selectors import ChatGPTVariables as CGPTV
from flask import Flask, request, jsonify
from markupsafe import escape
import argparse
import os
import json


class Bot(ChatGPT):
    def new_chat(self) -> None:
        """
        Create a new chat.
        """
        if not self.driver.current_url.startswith("https://chat.openai.com/"):
            return self.logger.debug("Current URL is not chat page, skipping create new chat")

        self.logger.debug("Creating new chat...")
        button = CGPTV.new_chat
        clicked = self.driver.safe_click(button, timeout=60)
        if not clicked:
            self.logger.debug(f"{button[1]} button not found")
            return self._get_out_of_menu()
        self.driver.refresh()
        self.logger.debug("New chat created")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='path to the configuration file')

    args = parser.parse_args()
    config_path = os.path.realpath(args.config) if args.config else (
        os.path.join(os.path.split(os.path.realpath(__file__))[0], 'config.json'))
    print(f"Configuration file path: {config_path}")

    with open(config_path) as f:
        config = json.loads(f.read())

    bot = Bot(
        session_token=config['ChatGPT']['session_token'],
        conversation_id=config['ChatGPT']['conversation_id'],
        proxy=config['ChatGPT']['proxy'],
        chrome_args=config['ChatGPT']['chrome_args'],
        disable_moderation=config['ChatGPT']['disable_moderation'],
        verbose=config['ChatGPT']['verbose'],
    )

    app = Flask(__name__)

    @app.route('/send_message', methods=['POST'])
    def send_message():
        response = {'status': {'failed': False, 'exception': ''}, 'message': ''}
        try:
            data = request.get_json()
            input_message = escape(data['message'])

            bot.new_chat()
            output_message = bot.send_message(input_message,
                                              input_mode=config['ChatGPT']['send_message']['input_mode'],
                                              input_delay=config['ChatGPT']['send_message']['input_delay'])

            if output_message.failed:
                response['status']['failed'] = True
            else:
                response['message'] = output_message.response
            return jsonify(response)

        except Exception as e:
            response['status']['failed'] = True
            response['status']['exception'] = str(e)
            return jsonify(response)

    app.run()


if __name__ == '__main__':
    main()
