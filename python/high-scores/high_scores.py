class HighScores:
    def __init__(self, scores):
        self._scores = scores

    @property
    def scores(self):
        return self._scores

    def latest(self):
        return self._scores[-1]

    def personal_best(self):
        return max(self._scores)

    def personal_top_three(self):
        sorted_scores = sorted(self._scores, reverse=True)
        return sorted_scores[0:3]
