class EntityManager:
    entities: dict
    _next_entity_id: int

    def __init__(self):
        self.entities = {}
        self._next_entity_id = 0

    def create_entity(self) -> int:
        entity_id = self._next_entity_id
        self.entities[entity_id] = {}
        self._next_entity_id += 1
        return entity_id

    def add_component(self, entity_id, component):
        self.entities[entity_id] [type(component)] = component
    
    def get_component(self, entity_id, *component_type):
        components = self.entities.get(entity_id, {})
        return (components.get (ct) for ct in component_type)
    
    def get_entities_with(self, *component_type):
        for entity_id, components in self.entities.items():
            if all(ct in components for ct in component_types):
                yield entity_id, [components[ct] for ct in component_types]