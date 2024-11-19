# pocket-tools
Python-powered toolkit to supercharge your pocket experience! 🛠️ easily manage, organize, and export your saved links and articles with advanced search, tagging, and more.

# Project structure

# Pocket API Authorization Guide

You need to acomplish following steps in order to get access token for your application.

## Step 1: Register Your Application

1. Visit [Pocket Developers Signup](https://getpocket.com/developer/apps/new.php?&src=signup).
2. Set your app permissions:
   - **Read Only**: if the app only retrieves data.
   - **Add, Modify**: if the app also adds or modifies data.
3. Note down the generated `consumer_key`.

## Step 2: Obtain a Request Token

1. Run the following `curl` command to request a `request_token` (replace YOUR_CONSUMER_KEY with your application's key. replace redirect_uri with the url of your application or leave it as it is if you are working in CLI, as we do in this case):

```bash
curl https://getpocket.com/v3/oauth/request -X POST \
-H "Content-Type: application/json" \
-H "X-Accept: application/json" \
-d "{\"consumer_key\":\"YOUR_CONSUMER_KEY\",\"redirect_uri\":\"urn:ietf:wg:oauth:2.0:oob\"}"
```
2. You will receive a response in JSON format, e.g. (note the your_request_token value.) use it in the next step:

```json
{"code":"your_request_token"}
```

## Step 3: Authorize the Application

1. Paste the following link to the browser (paste token from the previous step in place of "your_request_token"):

```bash
https://getpocket.com/auth/authorize?request_token=your_request_token&redirect_uri=urn:ietf:wg:oauth:2.0:oob
```

2. Open the link and authorize the application.
3. After successful authorization, you will see a confirmation message. No further action in the browser is needed.

## Step 4: Exchange the Request Token for an Access Token

1. Run the following curl command:

- Replace:
    - YOUR_CONSUMER_KEY with your app's key.
    - your_request_token with the token from Step 2.

```bash
curl https://getpocket.com/v3/oauth/authorize -X POST \
-H "Content-Type: application/json" \
-H "X-Accept: application/json" \
-d "{\"consumer_key\":\"YOUR_CONSUMER_KEY\",\"code\":\"your_request_token\"}"
```

2. You will receive a response containing the access_token and the username:

```json
{"access_token":"your_access_token","username":"user_name"}
```
* Save the access_token – it will be needed for API requests.

## Security Tips

- Store keys and tokens securely: Use configuration files with appropriate permissions.
- Avoid `--insecure` in curl commands: Unless testing in a trusted local environment.
- Do not publish consumer_key or access_token: Keep them private and out of public repositories.

# Installation

Create isolated Python environment if you wish to - please refer to my [article](https://skaczmarek-dev.github.io/posts/python-venv/).

Clone repository:

```
$ git clone https://github.com/skaczmarek-dev/pocket-tools
```

Install dependencies:

```
$ pip install -r pocket-tools/requirements.txt
```

## Prepare configuration file

Create file `config/settings.json` with following credentials obtained in step 2. and 4.:

```json
{
    "consumer_key":"YOUR_CONSUMER_KEY",
    "access_token":"YOUR_ACCESS_TOKEN",
    "detailType": "complete"
}
```

# How to run this program

```
cd pocket-tools
```
```
python3 main.py
```
```
python3 ./tests/test_pocket.py
```
