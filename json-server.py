import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import (
    retrieve_post,
    list_posts,
    login_user,
    create_category,
    list_categories,
    delete_category,
    update_category,
    create_user,
    list_tags,
)


class JSONServer(HandleRequests):
    def do_GET(self):

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "posts":
            if url["pk"] != 0:
                response_body = retrieve_post(url)
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_posts(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        if url["requested_resource"] == "tags":
            
            response_body = list_tags()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)


        if url["requested_resource"] == "categories":
            if url["pk"] != 0:
                response_body = ""
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_categories(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

    def do_POST(self):
        # this is the login logic for user
        if self.path == "/login":

            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            user_data = json.loads(body)
            print(user_data)
            response = login_user(user_data)
            print(response)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        # below will parse the self.path to dictionary so that python can exicute nessecary conditional logic for tickets
        url = self.parse_url(self.path)
        pk = url["pk"]
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "categories":
            successfully_posted = create_category(request_body)
            if successfully_posted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

            return self.response(
                "Requested resource not found",
                status.HTTP_500_SERVER_ERROR.value,
            )

        if url["requested_resource"] == "users":
            successfully_posted = create_user(request_body)
            if successfully_posted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

            return self.response(
                "Requested resource not found",
                status.HTTP_500_SERVER_ERROR.value,
            )

    def do_DELETE(self):
        """Handle DELETE requests from a client"""
        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "categories":
            if pk != 0:
                successfully_posted = delete_category(pk)
                if successfully_posted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        else:
            self.send_error(404)

    def do_PUT(self):
        url = self.parse_url(self.path)
        pk = url["pk"]

        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "categories":
            if pk != 0:
                successfully_updated = update_category(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )


def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
