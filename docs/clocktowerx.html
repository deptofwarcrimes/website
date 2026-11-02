<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clock Tower X (CTX) | Relational Topology Map</title>
  <style>
    :root {
      --bg: #070d18;
      --card-bg: rgba(14, 25, 44, 0.82);
      --card-border: #1e3352;
      --text-main: #f0f6fc;
      --text-muted: #8b9eb7;
      --accent-cyan: #38bdf8;
      --accent-purple: #c084fc;
      --accent-amber: #fbbf24;
      --accent-rose: #fb7185;
      --accent-emerald: #34d399;
      --font-mono: 'IBM Plex Mono', 'Cascadia Code', monospace;
      --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      background-image: 
        radial-gradient(ellipse at 50% 0%, rgba(56, 189, 248, 0.08) 0%, transparent 60%),
        linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
      background-size: 100% 100%, 32px 32px, 32px 32px;
      color: var(--text-main);
      font-family: var(--font-sans);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      padding: 24px 32px;
      border-bottom: 1px solid var(--card-border);
      background: rgba(7, 13, 24, 0.85);
      backdrop-filter: blur(12px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
    }

    .brand-title {
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-pill {
      font-family: var(--font-mono);
      font-size: 0.65rem;
      padding: 4px 8px;
      border-radius: 6px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid var(--accent-cyan);
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .controls {
      display: flex;
      gap: 10px;
    }

    .btn {
      background: #111f33;
      border: 1px solid #233b5c;
      color: var(--text-muted);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn:hover, .btn.active {
      background: #1b3152;
      border-color: var(--accent-cyan);
      color: var(--text-main);
    }

    .main-container {
      display: grid;
      grid-template-columns: 1fr 340px;
      flex: 1;
      position: relative;
    }

    #viewport {
      width: 100%;
      height: calc(100vh - 80px);
      position: relative;
      overflow: hidden;
      cursor: grab;
    }

    #viewport:active {
      cursor: grabbing;
    }

    svg#canvas {
      width: 100%;
      height: 100%;
    }

    /* Edge Links Styling */
    .link-path {
      fill: none;
      stroke-width: 1.75;
      stroke-linecap: round;
      transition: stroke 0.3s, stroke-width 0.3s, opacity 0.3s;
    }

    .link-path.fara { stroke: var(--accent-purple); stroke-dasharray: 6 3; }
    .link-path.infra { stroke: var(--accent-cyan); }
    .link-path.geo { stroke: #0284c7; stroke-dasharray: 4 4; }
    .link-path.sms { stroke: var(--accent-amber); }
    .link-path.reported { stroke: var(--accent-rose); stroke-dasharray: 2 4; }

    .link-text {
      font-family: var(--font-mono);
      font-size: 8px;
      fill: var(--text-muted);
      text-anchor: middle;
      pointer-events: none;
      letter-spacing: 0.5px;
    }

    /* Node Entities */
    .node-group {
      cursor: pointer;
    }

    .node-group circle {
      transition: r 0.2s ease, filter 0.2s ease, stroke-width 0.2s ease;
    }

    .node-group:hover circle {
      stroke-width: 3px;
      filter: drop-shadow(0 0 10px currentColor);
    }

    .node-label {
      font-size: 11px;
      font-weight: 600;
      fill: var(--text-main);
      pointer-events: none;
      text-shadow: 0 2px 6px rgba(0,0,0,0.8);
    }

    .node-subtext {
      font-family: var(--font-mono);
      font-size: 9px;
      fill: var(--text-muted);
      pointer-events: none;
    }

    /* Detail Sidebar */
    .sidebar {
      border-left: 1px solid var(--card-border);
      background: rgba(10, 18, 32, 0.95);
      backdrop-filter: blur(16px);
      padding: 24px;
      overflow-y: auto;
      height: calc(100vh - 80px);
      box-shadow: -10px 0 30px rgba(0,0,0,0.4);
    }

    .meta-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 20px;
    }

    .meta-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 8px;
      display: inline-block;
      font-weight: 700;
    }

    .meta-title {
      font-size: 1.15rem;
      font-weight: 800;
      margin-bottom: 6px;
      line-height: 1.3;
    }

    .meta-prop {
      margin-top: 12px;
    }

    .meta-prop-label {
      font-size: 0.7rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-family: var(--font-mono);
      margin-bottom: 2px;
    }

    .meta-prop-val {
      font-size: 0.85rem;
      color: #e2e8f0;
      line-height: 1.5;
    }

    /* Legend Box */
    .legend-box {
      display: grid;
      gap: 8px;
      font-size: 0.75rem;
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--text-muted);
    }

    .legend-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    /* Edge Flow Markers */
    marker#arrow-fara path { fill: var(--accent-purple); }
    marker#arrow-infra path { fill: var(--accent-cyan); }
    marker#arrow-geo path { fill: #0284c7; }
    marker#arrow-sms path { fill: var(--accent-amber); }
    marker#arrow-reported path { fill: var(--accent-rose); }
  </style>
</head>
<body>

  <header>
    <div class="brand-title">
      <span>CLOCK TOWER X</span>
      <span class="brand-pill">Topology Explorer</span>
    </div>
    <div class="controls">
      <button class="btn active" onclick="filterGraph('all')">View All</button>
      <button class="btn" onclick="filterGraph('fara')">FARA Lineage</button>
      <button class="btn" onclick="filterGraph('geo')">GEO Mesh</button>
      <button class="btn" onclick="filterGraph('sms')">SMS / Distribution</button>
      <button class="btn" onclick="resetZoom()">Reset View</button>
    </div>
  </header>

  <div class="main-container">
    <div id="viewport">
      <svg id="canvas">
        <defs>
          <marker id="arrow-fara" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" />
          </marker>
          <marker id="arrow-infra" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" />
          </marker>
          <marker id="arrow-geo" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" />
          </marker>
          <marker id="arrow-sms" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" />
          </marker>
          <marker id="arrow-reported" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1.5 L 8 5 L 0 8.5 z" />
          </marker>
        </defs>
        <g id="transform-group">
          <g id="links-layer"></g>
          <g id="nodes-layer"></g>
        </g>
      </svg>
    </div>

    <aside class="sidebar">
      <div id="inspector">
        <div class="meta-card">
          <span class="meta-tag" id="ent-cat" style="color: var(--accent-cyan);">ENTITY DETAILS</span>
          <h2 class="meta-title" id="ent-name">Select an Entity</h2>
          <div class="meta-prop">
            <div class="meta-prop-label">Classification / Role</div>
            <div class="meta-prop-val" id="ent-role">Click any node in the topology view to inspect its connections, registration records, and hosting telemetry.</div>
          </div>
          <div class="meta-prop">
            <div class="meta-prop-label">Infrastructure / Identifiers</div>
            <div class="meta-prop-val" id="ent-aux">—</div>
          </div>
          <div class="meta-prop">
            <div class="meta-prop-label">Recorded Linkage Details</div>
            <div class="meta-prop-val" id="ent-rel">—</div>
          </div>
        </div>
      </div>

      <div class="meta-card">
        <span class="meta-tag" style="color: var(--text-muted);">TOPOLOGY CLASSIFICATION</span>
        <div class="legend-box">
          <div class="legend-item">
            <span class="legend-dot" style="background: var(--accent-rose);"></span>
            <span>Clock Tower X Core Hub</span>
          </div>
          <div class="legend-item">
            <span class="legend-dot" style="background: var(--accent-purple);"></span>
            <span>FARA Principals & Brokers</span>
          </div>
          <div class="legend-item">
            <span class="legend-dot" style="background: var(--accent-cyan);"></span>
            <span>Technical / Hosting Ingress</span>
          </div>
          <div class="legend-item">
            <span class="legend-dot" style="background: #0284c7;"></span>
            <span>GEO Citation Mesh Fronts</span>
          </div>
          <div class="legend-item">
            <span class="legend-dot" style="background: var(--accent-amber);"></span>
            <span>Conversational Outreach & SMS</span>
          </div>
          <div class="legend-item">
            <span class="legend-dot" style="background: #eab308;"></span>
            <span>Campaign Partnerships</span>
          </div>
        </div>
      </div>
    </aside>
  </div>

  <script>
    // Topology Node Definitions
    const NODES = [
      // Central Node
      { id: 9, label: "Clock Tower X LLC", cat: "FARA Registrant", role: "Core Management & Digital Strategy Desk", color: "var(--accent-rose)", x: 500, y: 380, r: 18, aux: "FARA #7649 · Sole Owner: Bradley Parscale" },
      
      // FARA / Principal Track
      { id: 43, label: "Bradley Parscale", cat: "Beneficial Owner", role: "Disclosed 100% Sole Owner", color: "var(--accent-purple)", x: 260, y: 440, r: 13, aux: "Sole Controlling Principal" },
      { id: 6, label: "Havas Media Germany", cat: "Intermediary Broker", role: "Channels Campaign Budgets", color: "var(--accent-purple)", x: 260, y: 300, r: 14, aux: "$9M - $4.5M/Mo Allocation Desk" },
      { id: 1, label: "State of Israel (MFA/LAPAM)", cat: "Foreign Principal", role: "Foreign Sovereign Sponsor", color: "var(--accent-purple)", x: 80, y: 300, r: 16, aux: "Israeli Foreign Ministry Direct Directive" },
      
      // Core Technical Infrastructure (Direct CTX Subdomains)
      { id: 18, label: "clocktowerx.com", cat: "Registrant Website", role: "Official Public Web Destination", color: "var(--accent-cyan)", x: 500, y: 220, r: 12, aux: "Privacy policy discloses CTX corporate ownership" },
      { id: 19, label: "command.clocktowerx.com", cat: "Operational Console", role: "Multi-Client Ops Workspace", color: "var(--accent-cyan)", x: 400, y: 150, r: 10, aux: "Vercel Edge · 216.150.1.193" },
      { id: 20, label: "autodiscover.clocktowerx.com", cat: "Identity Nexus", role: "Exchange Online Admin / Identity Ingress", color: "var(--accent-cyan)", x: 670, y: 240, r: 14, aux: "M365 Tenant · 52.96.87.248" },
      { id: 21, label: "link.email.clocktowerx.com", cat: "Telemetry Router", role: "Outbound Click & Email Telemetry", color: "var(--accent-cyan)", x: 380, y: 250, r: 10, aux: "AWS CloudFront · ga.dyspatchit.net" },
      { id: 22, label: "forms.clocktowerx.com", cat: "Pipeline Intake", role: "Form Submission Qualification", color: "var(--accent-cyan)", x: 620, y: 160, r: 10, aux: "Cloudflare Ingress · 104.21.26.78" },
      { id: 23, label: "events.clocktowerx.com", cat: "Scheduling Desk", role: "Event Engagement Ingress", color: "var(--accent-cyan)", x: 520, y: 120, r: 10, aux: "Cloudflare Ingress · 172.67.135.161" },

      // GEO Mesh Network Fronts (Mapped to Node 20)
      { id: 24, label: "allyvia.org", cat: "GEO Think Tank", role: "Defense Pact / Strategic Front", color: "#0284c7", x: 860, y: 80, r: 9, aux: "Mail: allyvia-privacy@clocktowerx.com" },
      { id: 25, label: "paxpoint.org", cat: "GEO Think Tank", role: "Regional Accords Institute", color: "#0284c7", x: 890, y: 130, r: 9, aux: "Mail: paxpoint-privacy@clocktowerx.com" },
      { id: 26, label: "econora.org", cat: "GEO Think Tank", role: "Trade & Venture Policy Front", color: "#0284c7", x: 910, y: 180, r: 9, aux: "Mail: econora-privacy@clocktowerx.com" },
      { id: 27, label: "innovascope.org", cat: "GEO Think Tank", role: "Cyber Partnerships Front", color: "#0284c7", x: 920, y: 230, r: 9, aux: "Mail: innovascope-privacy@clocktowerx.com" },
      { id: 28, label: "culturavia.org", cat: "GEO Think Tank", role: "Evangelical Faith Outreach", color: "#0284c7", x: 910, y: 280, r: 9, aux: "Mail: culturavia-privacy@clocktowerx.com" },
      { id: 29, label: "justorium.org", cat: "GEO Legal Front", role: "Military Ethics / IHL Front", color: "#0284c7", x: 890, y: 330, r: 9, aux: "Mail: justorium-privacy@clocktowerx.com" },
      { id: 30, label: "cognitura.org", cat: "GEO Research Front", role: "Radicalization Research Desk", color: "#0284c7", x: 860, y: 380, r: 9, aux: "Mail: cognitura-privacy@clocktowerx.com" },
      { id: 31, label: "compassionpulse.org", cat: "GEO Humanitarian Front", role: "Aid & Corridor Documentation", color: "#0284c7", x: 820, y: 420, r: 9, aux: "Mail: compassionpulse-privacy@clocktowerx.com" },
      { id: 32, label: "factsignal.org", cat: "GEO Media Audit", role: "Counter-Disinformation Audit", color: "#0284c7", x: 770, y: 450, r: 9, aux: "Mail: info-factsignal@clocktowerx.com" },

      // Outreach & SMS Pipeline Branch
      { id: 33, label: "thetruthaboutiran.com", cat: "Targeted Outreach", role: "Regional Threat Intel & Campaign Desk", color: "var(--accent-amber)", x: 580, y: 530, r: 12, aux: "FARA #7649 Declared Asset" },
      { id: 34, label: "alliesforpeace.com", cat: "Targeted Outreach", role: "Conversational Media Dispatch Anchor", color: "var(--accent-amber)", x: 740, y: 560, r: 12, aux: "Shared contact: info@alliesforpeace.com" },
      { id: 35, label: "SparkFire Technologies", cat: "Conversational SMS", role: "Automated AI SMS Shortcode Engine", color: "var(--accent-amber)", x: 910, y: 560, r: 13, aux: "$6M Subcontract Execution Platform" },

      // External Political / Reported Link
      { id: 126, label: "Campaign Nucleus", cat: "Campaign Service", role: "Platform Founded by B. Parscale", color: "#eab308", x: 130, y: 490, r: 12, aux: "Reported Digital Campaign Provider" },
      { id: 125, label: "Influenceable LLC", cat: "Influencer Marketing", role: "Conservative Influencer Recruiter", color: "#eab308", x: 130, y: 590, r: 12, aux: "Texas Tribune reported promotional partnership" }
    ];

    // Topology Link Definitions
    const LINKS = [
      // FARA Track
      { s: 43, t: 9, lbl: "100% SOLE OWNER", type: "fara", marker: "arrow-fara" },
      { s: 9, t: 1, lbl: "REPRESENTS (FARA #7649)", type: "fara", marker: "arrow-fara" },
      { s: 9, t: 6, lbl: "ROUTED THROUGH", type: "fara", marker: "arrow-fara" },
      { s: 6, t: 1, lbl: "CONTRACTED BY", type: "fara", marker: "arrow-fara" },

      // Core Technical Subdomains
      { s: 9, t: 18, lbl: "OFFICIAL SITE", type: "infra", marker: "arrow-infra" },
      { s: 9, t: 19, lbl: "OPS CONSOLE", type: "infra", marker: "arrow-infra" },
      { s: 9, t: 20, lbl: "IDENTITY / MAIL NEXUS", type: "infra", marker: "arrow-infra" },
      { s: 9, t: 21, lbl: "TELEMETRY", type: "infra", marker: "arrow-infra" },
      { s: 9, t: 22, lbl: "INBOUND FORMS", type: "infra", marker: "arrow-infra" },
      { s: 9, t: 23, lbl: "SCHEDULING DESK", type: "infra", marker: "arrow-infra" },

      // Mail Nexus routing to GEO Mesh
      { s: 20, t: 24, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 25, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 26, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 27, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 28, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 29, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 30, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 31, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },
      { s: 20, t: 32, lbl: "MANAGED MAILBOX", type: "geo", marker: "arrow-geo" },

      // Outreach & SMS Pipeline
      { s: 9, t: 33, lbl: "DISCLOSED ASSET", type: "sms", marker: "arrow-sms" },
      { s: 33, t: 34, lbl: "CONTENT RELAY", type: "sms", marker: "arrow-sms" },
      { s: 34, t: 35, lbl: "DISPATCH ENGINE", type: "sms", marker: "arrow-sms" },

      // External Contextual Connections
      { s: 43, t: 126, lbl: "FOUNDER", type: "reported", marker: "arrow-reported" },
      { s: 126, t: 125, lbl: "REPORTED PARTNERSHIP", type: "reported", marker: "arrow-reported" }
    ];

    const svg = document.getElementById("canvas");
    const transformGroup = document.getElementById("transform-group");
    const linksLayer = document.getElementById("links-layer");
    const nodesLayer = document.getElementById("nodes-layer");

    // Pan & Zoom State
    let zoomLevel = 1.0;
    let panX = 0, panY = 0;
    let isDragging = false;
    let startX = 0, startY = 0;

    function renderTopology() {
      linksLayer.innerHTML = "";
      nodesLayer.innerHTML = "";

      // Draw Edges
      LINKS.forEach(link => {
        const source = NODES.find(n => n.id === link.s);
        const target = NODES.find(n => n.id === link.t);
        if (!source || !target) return;

        // Path
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        const dx = target.x - source.x;
        const dy = target.y - source.y;
        const dr = Math.sqrt(dx * dx + dy * dy) * 1.25;

        // Curved line
        path.setAttribute("d", `M ${source.x} ${source.y} A ${dr} ${dr} 0 0 1 ${target.x} ${target.y}`);
        path.setAttribute("class", `link-path ${link.type}`);
        path.setAttribute("marker-end", `url(#${link.marker})`);
        path.setAttribute("id", `link-${link.s}-${link.t}`);
        linksLayer.appendChild(path);

        // Text label on path
        const midX = (source.x + target.x) / 2;
        const midY = (source.y + target.y) / 2;
        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", midX);
        text.setAttribute("y", midY - 6);
        text.setAttribute("class", "link-text");
        text.textContent = link.lbl;
        linksLayer.appendChild(text);
      });

      // Draw Nodes
      NODES.forEach(node => {
        const group = document.createElementNS("http://www.w3.org/2000/svg", "g");
        group.setAttribute("class", "node-group");
        group.setAttribute("transform", `translate(${node.x}, ${node.y})`);
        group.onclick = () => inspectEntity(node);

        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("r", node.r);
        circle.setAttribute("fill", "#0a1322");
        circle.setAttribute("stroke", node.color);
        circle.setAttribute("stroke-width", "2");

        const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
        label.setAttribute("class", "node-label");
        label.setAttribute("x", node.r + 7);
        label.setAttribute("y", 3);
        label.textContent = node.label;

        const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
        sub.setAttribute("class", "node-subtext");
        sub.setAttribute("x", node.r + 7);
        sub.setAttribute("y", 15);
        sub.textContent = node.cat;

        group.appendChild(circle);
        group.appendChild(label);
        group.appendChild(sub);
        nodesLayer.appendChild(group);
      });
    }

    function inspectEntity(node) {
      document.getElementById("ent-name").textContent = node.label;
      document.getElementById("ent-cat").textContent = node.cat;
      document.getElementById("ent-cat").style.color = node.color;
      document.getElementById("ent-role").textContent = node.role;
      document.getElementById("ent-aux").textContent = node.aux || "None documented";

      // Calculate Direct Relationships
      const related = LINKS.filter(l => l.s === node.id || l.t === node.id);
      let summary = related.map(l => {
        const isSource = l.s === node.id;
        const otherId = isSource ? l.t : l.s;
        const other = NODES.find(n => n.id === otherId);
        return `• ${l.lbl} ${isSource ? '→' : '←'} ${other ? other.label : otherId}`;
      }).join("<br>");

      document.getElementById("ent-rel").innerHTML = summary || "No direct links in focused view.";
    }

    function filterGraph(type) {
      document.querySelectorAll(".controls .btn").forEach(b => b.classList.remove("active"));
      event.target.classList.add("active");

      const paths = document.querySelectorAll(".link-path");
      paths.forEach(p => {
        if (type === "all") {
          p.style.opacity = "1";
        } else {
          p.style.opacity = p.classList.contains(type) ? "1" : "0.08";
        }
      });
    }

    // Pan & Zoom Handler
    const viewport = document.getElementById("viewport");

    viewport.addEventListener("mousedown", (e) => {
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    });

    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener("mouseup", () => {
      isDragging = false;
    });

    viewport.addEventListener("wheel", (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
      zoomLevel = Math.min(Math.max(0.4, zoomLevel * zoomFactor), 2.5);
      updateTransform();
    }, { passive: false });

    function updateTransform() {
      transformGroup.setAttribute("transform", `translate(${panX}, ${panY}) scale(${zoomLevel})`);
    }

    function resetZoom() {
      zoomLevel = 0.95;
      panX = 30;
      panY = 10;
      updateTransform();
    }

    // Init Viewport
    renderTopology();
    resetZoom();
    // Default inspect node #9
    inspectEntity(NODES[0]);
  </script>
</body>
</html>
