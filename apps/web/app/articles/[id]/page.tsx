import Link from "next/link";
import { notFound } from "next/navigation";

type Article = {
  id: number;
  source_id: number;
  title: string;
  subtitle: string | null;
  summary: string | null;
  content: string | null;
  author: string | null;
  topic: string | null;
  status: string | null;
  canonical_url: string | null;
  original_published_at: string | null;
  created_at: string;
  source?: {
    name?: string | null;
    domain?: string | null;
  };
};

const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:58000";

export const dynamic = "force-dynamic";

async function fetchArticle(id: string): Promise<Article | null> {
  const response = await fetch(`${apiBaseUrl}/articles/${id}`, { cache: "no-store" });
  if (!response.ok) {
    return null;
  }
  return response.json();
}

export default async function ArticleDetailPage({ params }: { params: { id: string } }) {
  const article = await fetchArticle(params.id);

  if (!article) {
    notFound();
  }

  const sourceLabel =
    article.source?.name ?? article.source?.domain ?? `Fonte #${article.source_id}`;
  const publishedAt = article.original_published_at ?? article.created_at;

  return (
    <main>
      <Link className="back-link" href="/">
        ← Voltar para artigos
      </Link>
      <div className="detail">
        <h1>{article.title}</h1>
        {article.subtitle && <h2>{article.subtitle}</h2>}
        <div className="meta">
          <span>Fonte: {sourceLabel}</span>
          <span>Status: {article.status ?? "indefinido"}</span>
          <span>Publicado em: {new Date(publishedAt).toLocaleString("pt-BR")}</span>
        </div>
        {article.summary && <p>{article.summary}</p>}
        {article.content && <div>{article.content}</div>}
        {article.canonical_url && (
          <a href={article.canonical_url} target="_blank" rel="noreferrer">
            Ver fonte original
          </a>
        )}
      </div>
    </main>
  );
}
