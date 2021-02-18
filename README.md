## What is it?

This is an API template for Flask.  
Think of it as a shortcut for the project structure.

## Installation

```git clone``` i guess \^_\^  
Oh yes, also Python dependencies.  

In general, there is a little docker here.  
- Build docker image

```bash
docker build -t api-template .
```

- Run container

```bash
docker run --name test-api -p 5000:5000 --restart unless-stopped --env FLASK_ENV=development -d api-template
```

- Enjoy

```bash
curl http://127.0.0.1:5000
```

```json
{
  "ip": "172.17.0.1", 
  "status": true, 
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
```

There is also a [docker-compose.yml](/docker-compose.yml), I think you can figure it out yourself.
