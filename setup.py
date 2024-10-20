from setuptools import setup, find_packages

setup(
    name="custom_logging",  # Nome do pacote
    version="0.2",  # Versão do pacote
    description="Pacote de logging customizado",
    long_description=open("README.md").read(),  # Descrição longa (se você tiver um README)
    long_description_content_type="text/markdown",
    author="Guilherme Mello",
    author_email="guilhermesamello@gmail.com",
    url="https://github.com/gmellotec/custom_logging.git",  # URL do seu repositório GitHub
    packages=find_packages(),
    install_requires=["colorama"],  # Dependências necessárias para o pacote
)
