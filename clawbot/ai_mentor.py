class AIMentor:
    def __init__(self):
        self.templates = {
            'histogram': 'A histogram displays the distribution of volume over bars.',
            'gann': 'Gann analysis uses geometric, numeric, and time cycles in trading.',
            'astrology': 'Astrology analysis considers planetary positions for market prediction.'
        }

    def get_concept(self, concept):
        return self.templates.get(concept, 'Concept not found. Please add more templates.')
