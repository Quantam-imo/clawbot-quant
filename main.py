from clawbot.histogram import VolumeHistogram
from clawbot.gann_astrology import GannAstrology
from clawbot.ai_mentor import AIMentor

if __name__ == "__main__":
    # Example data
    bars = ['Bar1', 'Bar2', 'Bar3', 'Bar4']
    volumes = [100, 150, 120, 130]

    # 1. Volume Histogram
    vh = VolumeHistogram(volumes, bars)
    vh.plot()

    # 2. Gann and Astrology Analysis
    ga = GannAstrology()
    print(ga.analyze_gann(volumes))
    print(ga.analyze_astrology(volumes))

    # 3. AI Mentor
    mentor = AIMentor()
    for concept in ['histogram', 'gann', 'astrology']:
        print(f"{concept.title()} Concept: {mentor.get_concept(concept)}")
