# core/fourier_target_projection.py

import numpy as np
from scipy.fft import fft

class FourierTargetProjector:
    def __init__(self, target_profiles):
        """
        target_profiles: dict
            z.B. {"rekonfiguration": target_vector, "verbindung": target_vector, ...}
        """
        self.targets = {name: self._normalize(v) for name, v in target_profiles.items()}

    def _normalize(self, v):
        norm = np.linalg.norm(v)
        return v / norm if norm > 0 else v

    def transform_to_frequency_space(self, token_vectors):
        """
        Führt Fourier-Transformation auf Sequenz durch.
        token_vectors: np.ndarray [seq_len, dim]
        """
        return np.abs(fft(token_vectors, axis=0))  # Frequenzspektrum je Dimension

    def evaluate_resonance(self, spectrum, target_name):
        """
        Vergleicht Frequenzspektrum mit Zielvektor.
        spectrum: np.ndarray [freq_len, dim]
        """
        if target_name not in self.targets:
            raise ValueError(f"Zielprofil '{target_name}' nicht vorhanden.")

        target = self.targets[target_name]
        # Durchschnitt über Frequenzachsen, Korrelation mit Zielvektor
        avg_spectrum = np.mean(spectrum, axis=0)
        score = np.dot(self._normalize(avg_spectrum), target)
        return score

    def project_and_score(self, token_vectors, target_name):
        spectrum = self.transform_to_frequency_space(token_vectors)
        return self.evaluate_resonance(spectrum, target_name)
