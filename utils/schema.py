from drf_spectacular.openapi import AutoSchema as SpectacularAutoSchema


class AutoSchema(SpectacularAutoSchema):
    def get_tags(self):
        tokenized_path = self._tokenize_path()
        # use last non-parameter path part as default tag
        tag = tokenized_path[-1]
        
        # Convert kebab-case or snake_case to Title Case
        formatted_tag = tag.replace('-', ' ').replace('_', ' ').title()
        return [formatted_tag]
