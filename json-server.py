import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import (
    retrieve_post,
    list_posts, 
    login_user, create_post,
    create_category,
    list_categories,
    delete_category,
    update_category,
    create_user,
    list_tags,
    insert_tag,
    update_tag,
    delete_tag
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

        # below will parse the self.path to dictionary so that python can exicute nessecary conditional logic for tickets

        url = self.parse_url(self.path)
        pk = url["pk"]
        content_len = int(self.headers.get("content-length", 0))
        request_body_bytes = self.rfile.read(content_len)
        request_body_str = request_body_bytes.decode()  # Decode bytes to string
        request_body = json.loads(request_body_str)  # Parse JSON string to dict

        if self.path == "/login":
            user_data = request_body
            response = login_user(user_data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())



        if url["requested_resource"] == "categories":
            successfully_posted = create_category(request_body)
            if successfully_posted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            else:
                return self.response(
                "Requested resource not found",
                status.HTTP_500_SERVER_ERROR.value,
            )
        if url["requested_resource"] == "tags":
            if pk != 0:
                successfully_posted = update_tag(pk, request_body)
            else:
                successfully_posted = insert_tag(request_body)
            if successfully_posted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            else:
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
        
        # if url["requested_resource"] == "posts":
        #     successfully_posted = create_post(request_body)
        #     if successfully_posted:
        #         return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

        #     return self.response(
        #         "Requested resource not found",
        #         status.HTTP_500_SERVER_ERROR.value,
        #     )

        if url["requested_resource"] == "posts":
        # Call create_post with the request body
            post_creation_result = create_post(request_body)
        # Check if the post was successfully created
        if post_creation_result['valid']:
            # Return the entire response from create_post, including the token and valid flag
            return self.response(post_creation_result, status.HTTP_201_SUCCESS_CREATED.value)
        else:
            # If the post creation was not valid, return an error message
            return self.response(
                {"error": "Failed to create post."},
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
        elif url["requested_resource"] == "tags":
            if pk != 0:
                successfully_posted = delete_tag(pk)
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
