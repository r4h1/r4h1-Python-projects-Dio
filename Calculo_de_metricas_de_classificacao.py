# Colab Código Python para calcular as metricas de classificação e  plottar a curva ROC.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Função para calcular as metricas
def calcular_métricas(VP, VN, FP, FN):
    acuracia = (VP + VN) / (VP + VN + FP + FN)
    sensibilidade = VP / (VP + FN) if (VP + FN) != 0 else 0
    especificidade = VN / (VN + FP) if (VN + FP) != 0 else 0
    precisao = VP / (VP + FP) if (VP + FP) != 0 else 0
    f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) != 0 else 0
    
    return acuracia, sensibilidade, especificidade, precisao, f_score

# Função para plotar a curva ROC
def plotar_curva_roc(VP, VN, FP, FN):
    y_true = np.array([1] * VP + [0] * VN + [1] * FN + [0] * FP)
    y_scores = np.array([1] * (VP + FN) + [0] * (VN + FP))
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)
    
    plt.figure()
    plt.plot(fpr, tpr, color='blue', lw=2, label=f'Curva ROC (área = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.title('Curva ROC')
    plt.legend(loc='lower right')
    plt.show()

# Matriz de confusão arbitrária
VP = 50  # Verdadeiros Positivos
VN = 40  # Verdadeiros Negativos
FP = 10  # Falsos Positivos
FN = 20  # Falsos Negativos

# Cálculo das métricas
acuracia, sensibilidade, especificidade, precisao, f_score = calcular_métricas(VP, VN, FP, FN)

# Exibir os resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F-Score: {f_score:.2f}")

# Plotar a curva ROC
plotar_curva_roc(VP, VN, FP, FN)
