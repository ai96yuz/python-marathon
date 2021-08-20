import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import time

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

USERS_DICT = {k: v for element in USERS_LIST for k, v in element.items()}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])
        return json.loads(self.rfile.read(content_length).decode('utf-8'))

    def do_GET(self):
        json_result = USERS_LIST
        error_result = {
            "error": "User not found"
        }
        if self.path == '/users':
            return self._set_response(200, json_result)
        elif self.path == f'/user/{USERS_DICT.get("username")}':
            return self._set_response(200, USERS_DICT)
        return self._set_response(400, error_result)

    def do_POST(self):
        #   I hesitated with the decision because if in USERS_LIST there will be some users then it will be
        #   more correct to use: len(USERS_LIST[0]) & USERS_LIST[0]['id']
        #   Maybe this is not the right decision, I just want to say that I had two ideas for implementation.
        data_result = self._pars_body()
        empty_result = {}
        if self.path == '/user/createWithList':
            for el in data_result:
                if len(el) != len(USERS_DICT):
                    return self._set_response(400, empty_result)
                elif el.get('id') == USERS_DICT.get('id'):
                    return self._set_response(400, empty_result)
            return self._set_response(201, data_result)
        else:
            if len(data_result) != len(USERS_DICT):
                return self._set_response(400, empty_result)
            elif data_result.get('id') == USERS_DICT.get('id'):
                return self._set_response(400, empty_result)
            return self._set_response(201, data_result)

    def do_PUT(self):
        data_result = self._pars_body()
        if self.path == '/user/theUser':
            if len(data_result.keys()) != 5:
                result = {
                    "error": "not valid request data"
                }
                return self._set_response(400, result)
            else:
                return self._set_response(200, dict(**data_result, id=1))
        elif self.path == '/user/user_not_found':
            result = {
                "error": "User not found"
            }
            return self._set_response(404, result)

    def do_DELETE(self):
        error_result = {
            "error": "User not found"
        }
        empty_result = {}
        for el in USERS_LIST:
            if self.path == f'/user/{el.get("id")}':
                return self._set_response(200, empty_result)
            return self._set_response(404, error_result)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
