# Useage

### Env recommend
- python 3.10.6

### Quick Start
- git clone https://github.com/Linij/translate.git
- cd translate && python -m venv translate-env
- source translate-env/bin/activate
- python main.py 

### Test
`curl -X POST "http://localhost:8000/translate/zh-en" -H "Content-Type: application/json" -d '{"text": "你好,世界!"}'`

