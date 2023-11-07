from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        content_parsed = tomli.loads(content)
        poetry_content = content_parsed["tool"]["poetry"]

        authors_list = list(poetry_content["authors"])
        dev_dependencies_list = list(poetry_content["group"]["dev"]["dependencies"].keys())
        dependencies_list = list(poetry_content["dependencies"].keys())
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetry_content["name"], poetry_content["description"], poetry_content["license"], authors_list, dependencies_list, dev_dependencies_list)
