import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Para usar com seus dados reais: 
dados = json.load(open('./data/metricas.json'))[-10:]
q = [f"P{i+1:02d}" for i in range(len(dados))]
carga  = [d["carga_modelo_s"] for d in dados]
leit   = [d["leitura_prompt_s"] for d in dados]
gera   = [d["geracao_s"] for d in dados]
total  = [d["tempo_total_s"] for d in dados]
t_in   = [d["tokens_entrada"] for d in dados]
t_out  = [d["tokens_saida"] for d in dados]

BG, FG, GRID = "#0f172a", "#e2e8f0", "#334155"
C_CARGA, C_LEIT, C_GERA = "#f59e0b", "#38bdf8", "#a78bfa"
C_IN, C_OUT = "#34d399", "#fb7185"

plt.rcParams.update({"font.family":"DejaVu Sans","text.color":FG,"axes.labelcolor":FG,
                     "xtick.color":FG,"ytick.color":FG})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9.5), facecolor=BG,
                               gridspec_kw={"height_ratios":[1.35,1],"hspace":0.42})
for ax in (ax1, ax2):
    ax.set_facecolor(BG)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    for s in ("left","bottom"): ax.spines[s].set_color(GRID)
    ax.grid(axis="y", color=GRID, linewidth=0.7, alpha=0.7)
    ax.set_axisbelow(True)

fig.suptitle("Nexos | Desempenho no teste de histórico (10 perguntas)",
             fontsize=18, fontweight="bold", color=FG, y=0.975)
fig.text(0.5, 0.935, "Modelo llama3.2 via Ollama  •  histórico com as 5 últimas interações",
         ha="center", fontsize=11, color="#94a3b8")

# --- Painel 1: tempo empilhado ---
ax1.bar(q, carga, color=C_CARGA, label="Carga do modelo", width=0.62)
ax1.bar(q, leit, bottom=carga, color=C_LEIT, label="Leitura do prompt", width=0.62)
b2 = [c+l for c, l in zip(carga, leit)]
ax1.bar(q, gera, bottom=b2, color=C_GERA, label="Geração da resposta", width=0.62)
for i, t in enumerate(total):
    ax1.text(i, t+5, f"{t:.0f}s", ha="center", fontsize=10, fontweight="bold", color=FG)
ax1.set_ylabel("Tempo (segundos)")
ax1.set_ylim(0, max(total)*1.15)
ax1.set_title("Onde o tempo é gasto em cada pergunta", loc="left", fontsize=13, pad=12, color=FG)
ax1.legend(loc="upper right", frameon=False, ncol=3, labelcolor=FG, fontsize=10)

# --- Painel 2: tokens ---
ax2.plot(q, t_in, color=C_IN, marker="o", linewidth=2.5, label="Tokens de entrada (prompt)")
ax2.plot(q, t_out, color=C_OUT, marker="s", linewidth=2.5, label="Tokens de saída (resposta)")
ax2.axhline(2048, color="#94a3b8", linestyle="--", linewidth=1)
ax2.text(len(q)-0.6, 2048+110, "2048 tokens (contexto padrão do Ollama)", ha="right",
         fontsize=9, color="#94a3b8")
ax2.fill_between(q, t_out, color=C_OUT, alpha=0.12)
ax2.set_ylabel("Tokens")
ax2.set_ylim(0, max(t_in)*1.18)
ax2.set_title("Tamanho do prompt vs. tamanho da resposta", loc="left", fontsize=13, pad=12, color=FG)
ax2.legend(loc="upper right", frameon=False, ncol=2, labelcolor=FG, fontsize=10)

# --- Rodapé com KPIs ---
med = sorted(total)[len(total)//2-1:len(total)//2+1]
mediana = sum(med)/2
vel = sum(d["tokens_por_s"] for d in dados)/len(dados)
fig.text(0.5, 0.02,
         f"Tempo total mediano: {mediana:.0f}s   |   Mais lenta: {max(total):.0f}s (P03)   |   "
         f"Mais rápida: {min(total):.0f}s (P09)   |   Velocidade média: {vel:.1f} tokens/s",
         ha="center", fontsize=11, color=FG,
         bbox=dict(boxstyle="round,pad=0.6", fc="#1e293b", ec=GRID))

fig.savefig("grafico_performance_historico.png", dpi=170, facecolor=BG, bbox_inches="tight")
print("ok", mediana, vel)
