import "./globals.css";

export const metadata = {
  title: "Portal Política",
  description: "Portal Política - artigos e fontes"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
