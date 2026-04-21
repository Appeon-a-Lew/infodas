from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Requirement

GERMAN_STOPWORDS = {
    "aber","alle","allem","allen","aller","alles","als","also","am","an","ander","andere","anderem",
    "anderen","anderer","anderes","anderm","andern","anders","auch","auf","aus","bei","bin","bis",
    "bist","da","damit","dann","der","den","des","dem","die","das","dass","daß","derselbe","derselben",
    "denselben","desselben","demselben","dieselbe","dieselben","dasselbe","dazu","dein","deine","deinem",
    "deinen","deiner","deines","denn","derer","dessen","dich","dir","du","dies","diese","diesem","diesen",
    "dieser","dieses","doch","dort","durch","ein","eine","einem","einen","einer","eines","einig","einige",
    "einigem","einigen","einiger","einiges","einmal","er","ihn","ihm","es","etwas","euer","eure","eurem",
    "euren","eurer","eures","für","gegen","gewesen","hab","habe","haben","hat","hatte","hatten","hier",
    "hin","hinter","ich","mich","mir","ihr","ihre","ihrem","ihren","ihrer","ihres","euch","im","in",
    "indem","ins","ist","jede","jedem","jeden","jeder","jedes","jene","jenem","jenen","jener","jenes",
    "jetzt","kann","kein","keine","keinem","keinen","keiner","keines","können","könnte","machen","man",
    "manche","manchem","manchen","mancher","manches","mein","meine","meinem","meinen","meiner","meines",
    "mit","muss","musste","nach","nicht","nichts","noch","nun","nur","ob","oder","ohne","sehr","sein",
    "seine","seinem","seinen","seiner","seines","selbst","sich","sie","ihnen","sind","so","solche",
    "solchem","solchen","solcher","solches","soll","sollte","sondern","sonst","über","um","und","uns",
    "unse","unsem","unsen","unser","unses","unter","viel","vom","von","vor","während","war","waren",
    "warst","was","weg","weil","weiter","welche","welchem","welchen","welcher","welches","wenn","werde",
    "werden","wie","wieder","will","wir","wird","wirst","wo","wollen","wollte","würde","würden","zu",
    "zum","zur","zwar","zwischen",
}


class Shortlister:
    def __init__(self, corpus: list[Requirement], ngram_range: tuple[int, int] = (1, 2)) -> None:
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer(
            stop_words=list(GERMAN_STOPWORDS),
            ngram_range=ngram_range,
            min_df=1,
            sublinear_tf=True,
        )
        self.matrix = self.vectorizer.fit_transform(self._doc(r) for r in corpus)

    @staticmethod
    def _doc(r: Requirement) -> str:
        return f"{r.title}\n{r.text}"

    def top_k(self, query: Requirement, k: int = 15) -> list[tuple[Requirement, float]]:
        qv = self.vectorizer.transform([self._doc(query)])
        sims = cosine_similarity(qv, self.matrix).ravel()
        idx = sims.argsort()[::-1][:k]
        return [(self.corpus[i], float(sims[i])) for i in idx]


if __name__ == "__main__":
    from pathlib import Path
    from . import parse_gs, parse_gspp

    root = Path(__file__).resolve().parent.parent
    gs_reqs = parse_gs.parse(root / "data" / "gs.xml")
    gspp_reqs = parse_gspp.parse(root / "data" / "gspp.json")

    sl = Shortlister(gs_reqs)
    for q in gspp_reqs[:3]:
        print(f"\n== {q.id} {q.title} ==")
        for r, s in sl.top_k(q, k=5):
            print(f"  {s:.3f}  {r.id}  [{r.level}]  {r.title[:70]}")
    # sanity: GC.6.1.3 Erstellung einer Sicherheitsleitlinie should pull ISMS/ORP matches
    for q in gspp_reqs:
        if q.id == "GC.6.1.3":
            print(f"\n== sanity: {q.id} {q.title} ==")
            for r, s in sl.top_k(q, k=10):
                print(f"  {s:.3f}  {r.id}  [{r.level}]  {r.title[:70]}")
            break
