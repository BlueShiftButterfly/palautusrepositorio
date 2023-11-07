class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, items):
        return ("\n- " + "\n- ".join(items)) if len(items) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_list(self.authors)}"
            f"\n\nDependencies: {self._stringify_list(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_list(self.dev_dependencies)}"
        )
