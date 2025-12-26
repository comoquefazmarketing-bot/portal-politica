import Link from "next/link";

type Article = {
  id: number;
  source_id: number;
  title: string;
  status: string | null;
  original_published_at: string | null;
  created_at: string;
  source?: {
    name?: string | null;
    domain?: string | null;
  };
};

const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:58000";

export const dynamic = "force-dynamic";

async function fetchArticles(): Promise<Article[]> {
  const response = await fetch(`${apiBaseUrl}/articles`, { cache: "no-store" });
  if (!response.ok) {
    return [];
  }
  return response.json();
}

export default async function HomePage() {
  const articles = await fetchArticles();

  return (
    <main>
      <div className="header">
        <h1>Portal Política</h1>
        <p>Últimos artigos disponíveis</p>
      </div>

      {articles.length === 0 ? (
        <div className="empty">Sem artigos ainda</div>
      ) : (
        <div className="cards">
          {articles.map((article) => {
            const sourceLabel =
              article.source?.name ??
              article.source?.domain ??
              `Fonte #${article.source_id}`;
            const publishedAt = article.original_published_at ?? article.created_at;

            return (
              <Link key={article.id} href={`/articles/${article.id}`} className="card">
                <h2>{article.title}</h2>
                <div className="meta">
                  <span>Fonte: {sourceLabel}</span>
                  <span>Status: {article.status ?? "indefinido"}</span>
                  <span>
                    Publicado em: {new Date(publishedAt).toLocaleString("pt-BR")}
                  </span>
                </div>
              </Link>
            );
          })}
        </div>
      )}
    </main>
  );
}
