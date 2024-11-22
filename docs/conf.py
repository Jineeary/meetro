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

templates_path = ['_templates']  # 템플릿 경로
exclude_patterns = []  # 제외할 파일 및 디렉토리 패턴

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # HTML 테마 (다른 테마를 사용할 수도 있음)
html_static_path = ['_static']  # 정적 파일 경로

master_doc = 'index'  # 마스터 문서가 'index.rst'임을 명시
