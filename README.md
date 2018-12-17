# Stack overflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

# Features
1. Users can create an account and log in.
2. Users can post questions.
3. Users can delete the questions they post.
4. Users can post answers.
5. Users can view the answers to questions.
6. Users can accept an answer out of all the answers to his/her question as the preferred answer.

# Pages Link
[Stack overflow](https://bakley.github.io/Stackoverflow-lite/UI/view-questions.html)

## API Endpoints covered included in this branch


| Method        |       Endpoint                        |         Description                           |
| ------------- |       -------------                   |         -------------                         |
| `GET`         | `/api/v1/auth/user`                   |   Gets all the users                          |
| `GET`         | `/api/v1/auth/user/<userid>`          |   Get a user by id                            |
| `POST`        | `/api/v1/auth/signup`                 |   Register a user                             |
| `POST`        | `/api/v1/auth/login`                  |   Sign in a User                              |


