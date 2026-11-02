StudyPlace/
│
├── docs/
│   ├── README.md
│   ├── DATABASE.md
│   ├── USER_GUIDE.md
│   ├── FEATURES.md
│   ├── PROJECT_STRUCTURE.md
│   └── DEVELOPMENT_LOG.md
│
└── snippets/
    └── models.py

snippets/
└── templates/
    └── snippets/
        ├── home.html
        ├── snippet_form.html
        ├── detail.html
        └── delete_confirm.html
        
        
mkdir -p snippets/templates/snippets
mkdir -p snippets/static/snippets/css
mkdir -p snippets/static/snippets/js

touch snippets/templates/snippets/base.html
touch snippets/templates/snippets/home.html
touch snippets/templates/snippets/snippet_form.html
touch snippets/templates/snippets/detail.html
touch snippets/templates/snippets/delete_confirm.html

touch snippets/static/snippets/css/style.css
touch snippets/static/snippets/js/main.js