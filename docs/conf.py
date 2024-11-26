# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'meetro' 
author = 'Jineeary'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [  # Sphinx 확장 모듈
    'sphinx.ext.autodoc',    # 자동 문서화
    'sphinx.ext.napoleon',   # NumPy & Google 스타일 docstring 지원
]

language='Meetro_ossw24'
templates_path = ['_templates']  # 템플릿 경로
exclude_patterns = []  # 제외할 파일 및 디렉토리 패턴

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'  # 마스터 문서가 'index.rst'임을 명시
