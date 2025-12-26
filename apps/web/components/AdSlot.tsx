type AdSlotProps = {
  id: string;
  minHeight: number;
  className?: string;
};

function AdSlot({ id, minHeight, className }: AdSlotProps) {
  return (
    <div className={`ad-slot ${className ?? ""}`} style={{ minHeight }} data-slot-id={id}>
      <span className="ad-label">Publicidade</span>
      <div className="ad-placeholder">Ad Slot • {id}</div>
    </div>
  );
}

export function AdTop() {
  return <AdSlot id="top-leaderboard" minHeight={90} className="ad-top" />;
}

export function AdSidebar({ size = "large" }: { size?: "large" | "medium" }) {
  return (
    <AdSlot
      id={size === "large" ? "sidebar-rect-lg" : "sidebar-rect-md"}
      minHeight={size === "large" ? 600 : 250}
      className={`ad-sidebar ad-sidebar-${size}`}
    />
  );
}

export function AdInline() {
  return <AdSlot id="inline-rect" minHeight={250} className="ad-inline" />;
}

export function AdFooter() {
  return <AdSlot id="footer" minHeight={90} className="ad-footer" />;
}
