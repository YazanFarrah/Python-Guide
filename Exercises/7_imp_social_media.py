# Social media app

social_media_posts = []
while True:
    username = input("Enter ur username ").lower().strip()

    if username:
        print("1. Create a Post")
        print("2. Display all Posts")
        print("3. Display a User's Posts")
        print("Q. Press q to quit the application")
        option = int(input("Select ur option... "))
        if option == 1:
            title = input("Title of ur post: ")
            description = input("Description of ur post: ")
            post = {"title": title, "description": description, "username": username}
            social_media_posts.append(post)
            print("Post created.")
        elif option == 2:
            print("Posts:\n")
            for post in social_media_posts:
                print("------------------------------")
                print(post["username"])
                print(post["title"])
                print(post["description"])
                print("------------------------------")

        elif option == 3:
            search_user_query = input("Enter specific username").lower().strip()
            print(f"{search_user_query} Posts:\n")
            for post in social_media_posts:
                if post["username"] == search_user_query:
                    print("------------------------------")
                    print(post["username"])
                    print(post["title"])
                    print(post["description"])
                    print("------------------------------")
        else:
            break
