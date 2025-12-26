import { AdFooter, AdInline, AdSidebar, AdTop } from "../components/AdSlot";

const hypeCards = [
  {
    id: "hype-1",
    title: "Congresso pauta reforma administrativa em sessão extraordinária",
    summary: "Líderes discutem impacto fiscal e próximos passos no plenário."
  },
  {
    id: "hype-2",
    title: "Governos estaduais anunciam consórcio para infraestrutura verde",
    summary: "Parceria pretende acelerar projetos de energia limpa."
  },
  {
    id: "hype-3",
    title: "Câmara debate marco regulatório para plataformas digitais",
    summary: "Audiências públicas reúnem especialistas e representantes do setor."
  }
];

const moreNewsCards = [
  {
    id: "news-1",
    title: "Prefeituras ampliam orçamento participativo em 2025",
    summary: "Municípios apostam em ferramentas digitais para consulta pública."
  },
  {
    id: "news-2",
    title: "Relatório aponta avanço em transparência de gastos públicos",
    summary: "Ranking anual destaca boas práticas de dados abertos."
  },
  {
    id: "news-3",
    title: "Comissão discute metas climáticas para a próxima década",
    summary: "Propostas incluem incentivos à mobilidade urbana."
  },
  {
    id: "news-4",
    title: "Painel analisa cenário eleitoral e comunicação política",
    summary: "Especialistas falam sobre tendências de engajamento."
  }
];

export default function HomePage() {
  return (
    <main>
      <header className="header">
        <div>
          <span className="eyebrow">Portal Política</span>
          <h1>Panorama confiável para decisões informadas</h1>
          <p>Curadoria diária de temas públicos, legislação e políticas em destaque.</p>
        </div>
        <nav className="nav">
          <a href="/">Início</a>
          <a href="/">Hype</a>
          <a href="/">Categorias</a>
        </nav>
      </header>

      <AdTop />

      <div className="layout">
        <section className="feed">
          <section className="section">
            <div className="section-header">
              <h2>Hype Agora</h2>
              <span>Atualizado há poucos minutos</span>
            </div>
            <div className="cards">
              {hypeCards.map((card) => (
                <article key={card.id} className="card">
                  <h3>{card.title}</h3>
                  <p>{card.summary}</p>
                </article>
              ))}
            </div>
            <AdInline />
          </section>

          <section className="section">
            <div className="section-header">
              <h2>Mais Notícias</h2>
              <span>Seleção editorial</span>
            </div>
            <div className="cards">
              {moreNewsCards.map((card) => (
                <article key={card.id} className="card">
                  <h3>{card.title}</h3>
                  <p>{card.summary}</p>
                </article>
              ))}
            </div>
          </section>
        </section>

        <aside className="sidebar">
          <AdSidebar size="large" />
          <AdSidebar size="medium" />
        </aside>
      </div>

      <footer className="footer">
        <div className="footer-content">
          <div>
            <h2>Portal Política</h2>
            <p>Transparência, contexto e velocidade na cobertura política.</p>
          </div>
          <AdFooter />
        </div>
      </footer>
    </main>
  );
}
