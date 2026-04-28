import streamlit as st
import plotly.graph_objects as go

# ─── PAGE CONFIG ───────────────────────────────────────────
st.set_page_config(
    page_title="Paragon Network Dashboard",
    page_icon="📊",
    layout="wide",
)

# ─── COLOR DEFINITIONS ─────────────────────────────────────
C_BLUE = "#378ADD"
C_ORANGE = "#D85A30"
C_GREEN = "#639922"
C_PURPLE = "#534AB7"
C_TEXT = "#1a1a1a"
C_MUTED = "#7a85a8"
C_BORDER = "#e0e0e0"

# ─── PLOTLY LAYOUT DEFAULTS ───────────────────────────────
PLOTLY_LAYOUT = {
    "template": "plotly_white",
    "font": {"family": "system-ui, -apple-system, sans-serif", "color": C_TEXT, "size": 12},
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "margin": {"l": 0, "r": 0, "t": 30, "b": 0},
}

# ─── COLOR PALETTE (for consistent ordering) ────────────────
COLOR_PALETTE = [C_BLUE, C_ORANGE, C_GREEN, C_PURPLE, "#ff5b8c", "#ffb85b", "#5bffff", "#a8b8ff", "#ffb8d1", "#6b9a9a"]

# ─── HELPER FUNCTION: Sort data by value & assign colors ────
def sort_by_value(labels, values):
    """Sort labels and values by value (descending), return with consistent colors."""
    pairs = list(zip(labels, values))
    pairs.sort(key=lambda x: x[1], reverse=True)
    sorted_labels = [p[0] for p in pairs]
    sorted_values = [p[1] for p in pairs]
    sorted_colors = COLOR_PALETTE[:len(sorted_labels)]
    return sorted_labels, sorted_values, sorted_colors

# ─── CUSTOM CSS ────────────────────────────────────────────
st.markdown("""
    <style>
    /* Mobile-first responsive design */
    * {
        box-sizing: border-box;
    }
    
    .pill {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: 500;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    .pill-blue {
        background-color: #E6F1FB;
        color: #185FA5;
    }
    .pill-orange {
        background-color: #FAEEDA;
        color: #854F0B;
    }
    .pill-green {
        background-color: #EAF3DE;
        color: #3B6D11;
    }
    
    .report-section {
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .report-section h3 {
        margin-top: 0;
        margin-bottom: 0.75rem;
        font-size: 16px;
        font-weight: 600;
    }
    .report-section p {
        margin: 0.5rem 0;
    }
    
    .insight-box {
        padding: 12px 14px;
        border-radius: 8px;
        border-left: 4px solid;
        font-size: 13px;
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    .insight-box.blue {
        background-color: #E6F1FB;
        border-color: #185FA5;
        color: #042C53;
    }
    .insight-box.orange {
        background-color: #FAEEDA;
        border-color: #854F0B;
        color: #412402;
    }
    .insight-box.green {
        background-color: #EAF3DE;
        border-color: #3B6D11;
        color: #173404;
    }
    
    /* Charts responsive container */
    .chart-container {
        width: 100%;
        margin-bottom: 1rem;
    }
    
    /* Mobile: Stack all charts vertically */
    @media (max-width: 768px) {
        .chart-container {
            width: 100% !important;
        }
        .report-section {
            font-size: 13px;
        }
        .report-section h3 {
            font-size: 15px;
        }
        .insight-box {
            font-size: 12px;
            padding: 10px 12px;
        }
    }
    
    /* Tablet and up: Layout improves */
    @media (min-width: 769px) {
        .report-section {
            font-size: 14px;
        }
    }
    
    /* Desktop: Full layout */
    @media (min-width: 1200px) {
        .report-section {
            font-size: 14px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ─── PAGE: NETWORK ANALYSIS REPORT ───────────────────────
st.markdown("# Network Analysis Report")
st.markdown('<div style="color:#7a85a8; margin-bottom:1.5rem; font-size:0.9rem;">Paragon Network · Spring 2026 · Strategic analysis of speakers, government partners, and mentors.</div>', unsafe_allow_html=True)

# Quick-nav pills
st.markdown("""
<div style="margin-bottom:1.5rem;">
  <a href="#overall-network" style="text-decoration:none;">
    <span class="pill pill-blue">Overall Network</span>
  </a>
  <a href="#speakers" style="text-decoration:none;">
    <span class="pill pill-blue">Speakers</span>
  </a>
  <a href="#gov-partners" style="text-decoration:none;">
    <span class="pill pill-blue">Gov Partners</span>
  </a>
  <a href="#mentors" style="text-decoration:none;">
    <span class="pill pill-blue">Mentors</span>
  </a>
  <a href="#key-findings" style="text-decoration:none;">
    <span class="pill pill-orange">Key Findings</span>
  </a>
  <a href="#strengths" style="text-decoration:none;">
    <span class="pill pill-orange">Strengths</span>
  </a>
  <a href="#weaknesses" style="text-decoration:none;">
    <span class="pill pill-orange">Weaknesses</span>
  </a>
  <a href="#recommendations" style="text-decoration:none;">
    <span class="pill pill-green">Recommendations</span>
  </a>
</div>
""", unsafe_allow_html=True)

# ── OVERALL NETWORK ──
st.markdown('<div id="overall-network"></div>', unsafe_allow_html=True)
with st.expander("🌐 Overall Network", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="report-section">
          <h3>Overview</h3>
          <p>Paragon's evolving network is a core part of the organization — shaping who fellows learn from, the kinds of projects and partnerships that are possible, and which professional pathways are most visible and accessible.</p>
          <p>This report analyzes Paragon's existing network as of Spring 2026 to identify patterns, strengths, gaps, and opportunities for growth.</p>
          <p><strong>Network Composition:</strong> Professionals with 10+ years of experience make up the majority of Paragon's network.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        industries = ["Gov Partners", "Private", "AI", "Public Policy", "Nonprofit/Advocacy", "Research & Academia", "Other"]
        pcts = [32, 14, 11, 9, 9, 9, 16]
        industries, pcts, colors = sort_by_value(industries, pcts)
        fig = go.Figure(go.Pie(
            labels=industries, values=pcts, hole=0.55,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=11, color="white"),
            hovertemplate="%{label}: %{value}%<extra></extra>",
        ))
        fig.update_layout(**PLOTLY_LAYOUT, height=260, showlegend=True,
            legend=dict(font=dict(size=11), orientation="v", x=1.05, y=1))
        st.plotly_chart(fig, use_container_width=True)

    sectors = ["AI", "Civic/Gov Tech", "Public Policy", "Data & Analytics", "Legal", "Cybersecurity", "National Security", "Other"]
    sector_pcts = [19, 17, 12, 8, 7, 6, 5, 26]
    fig_sec = go.Figure(go.Bar(
        x=sectors, y=sector_pcts,
        marker_color=[C_BLUE, C_GREEN, C_ORANGE, C_PURPLE, "#ff5b8c", "#ffb85b", "#5bffff", "#6b9a9a"],
        marker_line_width=0,
        text=[f"{p}%" for p in sector_pcts],
        textposition="outside",
        textfont=dict(color=C_MUTED, size=11),
    ))
    fig_sec.update_layout(
        **PLOTLY_LAYOUT, height=260,
        title=dict(text="Network by Sector", font=dict(color="#378ADD", size=14), x=0.5, xanchor="center"),
        xaxis=dict(tickfont=dict(color="white", size=12)),
        yaxis=dict(tickfont=dict(color="white", size=11), gridcolor=C_BORDER, ticksuffix="%"),
    )
    st.plotly_chart(fig_sec, use_container_width=True)

# ── SPEAKERS ──
st.markdown('<div id="speakers"></div>', unsafe_allow_html=True)
with st.expander("🎤 Speakers", expanded=False):
    # Summary text at top
    st.markdown("""
    <div class="report-section">
      <h3>Speaker Network</h3>
      <p>Speakers are relatively diversified across sectors, with strong representation from Research & Academia, Private, and Nonprofit/Advocacy. Combined government representation (federal, state, and local) is substantial at 18%.</p>
      <p>By industry, AI, Public Policy, and Civic/Gov Tech lead. However, representation drops off significantly after these core areas — Legal and Data & Analytics are modestly represented, while Cybersecurity, National Security, and Media/Communications have minimal presence.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Three charts side-by-side
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        sp_industries = ["AI", "Public Policy", "Civic/Gov Tech", "Legal", "Data & Analytics", "Cybersecurity", "Nat. Security", "Media/Comms"]
        sp_pcts = [31, 25, 16, 9, 9, 3, 3, 3]
        fig = go.Figure(go.Bar(
            y=sp_industries, x=sp_pcts, orientation="h",
            marker_color=C_BLUE, marker_line_width=0,
            text=[f"{p}%" for p in sp_pcts], textposition="outside",
            textfont=dict(color="white", size=11),
        ))
        fig.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Speakers by Industry", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            xaxis=dict(showticklabels=False, showgrid=False),
            yaxis=dict(tickfont=dict(color="white", size=9), autorange="reversed"),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        sp_sectors = ["Research & Academia", "Private", "Nonprofit/Advocacy", "Think Tank", "Fed Gov", "State Gov", "Local Gov", "IGO", "Philanthropic"]
        sp_sector_pcts = [28, 22, 16, 6, 9, 6, 3, 3, 3]
        sp_sectors, sp_sector_pcts, colors = sort_by_value(sp_sectors, sp_sector_pcts)
        fig_sector = go.Figure(go.Pie(
            labels=sp_sectors, values=sp_sector_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=9, color="white"),
        ))
        fig_sector.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Speakers by Sector", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=9), x=1.05, y=0.5))
        st.plotly_chart(fig_sector, use_container_width=True)

    with col3:
        sp_exp = ["10+ years", "5-9 years", "3-5 years", "1-3 years"]
        sp_exp_pcts = [72, 19, 6, 3]
        sp_exp, sp_exp_pcts, colors = sort_by_value(sp_exp, sp_exp_pcts)
        fig_exp = go.Figure(go.Pie(
            labels=sp_exp, values=sp_exp_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=10, color="white"),
        ))
        fig_exp.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Speakers by Experience", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=10), x=1.05, y=0.5))
        st.plotly_chart(fig_exp, use_container_width=True)
    
    # Strengths and Gaps side-by-side at bottom
    col_strength, col_gap = st.columns(2)
    
    with col_strength:
        st.markdown("""
        <div class="insight-box green">
          <strong>✓ Strengths:</strong> Nearly 72% of speakers have 10+ years of experience, offering long-term career perspectives and exceptional credibility. Strong representation across both research and practitioner backgrounds provides diverse viewpoints.
        </div>
        """, unsafe_allow_html=True)
    
    with col_gap:
        st.markdown("""
        <div class="insight-box orange">
          <strong>⚠ Gaps:</strong> Early-career speakers are significantly underrepresented — only 3% have 1–3 years of experience. This limits relatable entry-level perspectives for fellows still navigating early stages of their careers.
        </div>
        """, unsafe_allow_html=True)

# ── GOVERNMENT PARTNERS ──
st.markdown('<div id="gov-partners"></div>', unsafe_allow_html=True)
with st.expander("🏛️ Government Partners", expanded=False):
    # Summary text at top
    st.markdown("""
    <div class="report-section">
      <h3>Government Partner Network</h3>
      <p>Government partners are concentrated primarily in local government (67%), followed by state (19%) and federal (4%). The remaining partners have transitioned to nonprofit/advocacy (7%) or private (4%) sectors.</p>
      <p>By industry, Civic/Gov Tech (37%) has dominant representation, followed by AI (19%) and Public Policy (15%). This concentration reflects Paragon's strong focus on technology and governance alignment.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Three charts side-by-side
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        gov_sectors = ["Local Gov", "State Gov", "Federal Gov", "Nonprofit/Advocacy", "Private"]
        gov_pcts = [67, 19, 4, 7, 4]
        gov_sectors, gov_pcts, colors = sort_by_value(gov_sectors, gov_pcts)
        fig = go.Figure(go.Pie(
            labels=gov_sectors, values=gov_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=9, color="white"),
        ))
        fig.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Gov Partners by Sector", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=10), x=1.05, y=0.5))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        gov_ind = ["Civic/Gov Tech", "AI", "Public Policy", "Data & Analytics", "Privacy", "National Security", "Media/Communications", "Education", "Healthcare/Biotech"]
        gov_ind_pcts = [37, 19, 15, 7, 7, 4, 4, 4, 4]
        gov_ind, gov_ind_pcts, colors = sort_by_value(gov_ind, gov_ind_pcts)
        fig_gov_ind = go.Figure(go.Pie(
            labels=gov_ind, values=gov_ind_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=9, color="white"),
        ))
        fig_gov_ind.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Gov Partners by Industry", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=9), x=1.05, y=0.5))
        st.plotly_chart(fig_gov_ind, use_container_width=True)

    with col3:
        gov_exp = ["10+ years", "5-9 years", "3-5 years"]
        gov_exp_pcts = [74, 22, 4]
        gov_exp, gov_exp_pcts, colors = sort_by_value(gov_exp, gov_exp_pcts)
        fig_gov_exp = go.Figure(go.Pie(
            labels=gov_exp, values=gov_exp_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=10, color="white"),
        ))
        fig_gov_exp.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Gov Partners by Experience", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=10), x=1.05, y=0.5))
        st.plotly_chart(fig_gov_exp, use_container_width=True)
    
    # Strengths and Gaps side-by-side at bottom
    col_strength, col_gap = st.columns(2)
    
    with col_strength:
        st.markdown("""
        <div class="insight-box green">
          <strong>✓ Strengths:</strong> Overwhelming majority (74%) have 10+ years of experience, providing exceptional credibility and depth. Strong local government focus creates opportunities for community-level implementation and real-world project partnerships.
        </div>
        """, unsafe_allow_html=True)
    
    with col_gap:
        st.markdown("""
        <div class="insight-box orange">
          <strong>⚠ Gaps:</strong> Severely limited state and federal government representation — only 19% and 4% respectively. This constrains Paragon's ability to engage with policy decisions at higher levels of government.
        </div>
        """, unsafe_allow_html=True)

# ── MENTORS ──
st.markdown('<div id="mentors"></div>', unsafe_allow_html=True)
with st.expander("🤝 Mentors", expanded=False):
    # Summary text at top
    st.markdown("""
    <div class="report-section">
      <h3>Mentor Network</h3>
      <p>The mentor network is the most balanced across sectors — Private (34%), Research & Academia (23%), Nonprofit/Advocacy (17%), and Federal Government (14%) are all well represented, providing diverse pathways and backgrounds.</p>
      <p>By industry, AI (37%), Public Policy (20%), and Civic/Gov Tech (17%) lead, with Legal, Cybersecurity, and Energy also represented. The experience distribution is notably more varied than speakers and government partners.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Three charts side-by-side
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        mentor_sectors = ["Private", "Research & Academia", "Nonprofit/Advocacy", "Federal Gov", "Other"]
        mentor_pcts = [34, 23, 17, 14, 12]
        mentor_sectors, mentor_pcts, colors = sort_by_value(mentor_sectors, mentor_pcts)
        fig = go.Figure(go.Pie(
            labels=mentor_sectors, values=mentor_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=9, color="white"),
        ))
        fig.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Mentors by Sector", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=10), x=1.05, y=0.5))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        mentor_ind = ["AI", "Public Policy", "Civic/Gov Tech", "Legal", "Cybersecurity", "Energy", "Other"]
        mentor_ind_pcts = [37, 20, 17, 11, 9, 6, 0]
        mentor_ind, mentor_ind_pcts, colors = sort_by_value(mentor_ind, mentor_ind_pcts)
        fig_mentor_ind = go.Figure(go.Pie(
            labels=mentor_ind, values=mentor_ind_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=9, color="white"),
        ))
        fig_mentor_ind.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Mentors by Industry", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=9), x=1.05, y=0.5))
        st.plotly_chart(fig_mentor_ind, use_container_width=True)

    with col3:
        mentor_exp = ["10+ years", "3-5 years", "1-3 years", "5-9 years"]
        mentor_exp_pcts = [31, 26, 23, 20]
        mentor_exp, mentor_exp_pcts, colors = sort_by_value(mentor_exp, mentor_exp_pcts)
        fig_mentor_exp = go.Figure(go.Pie(
            labels=mentor_exp, values=mentor_exp_pcts, hole=0.5,
            marker_colors=colors,
            textinfo="percent",
            textfont=dict(size=10, color="white"),
        ))
        fig_mentor_exp.update_layout(**PLOTLY_LAYOUT, height=320,
            title=dict(text="Mentors by Experience", font=dict(size=14, color="#378ADD"), x=0.5, xanchor="center"),
            showlegend=True, legend=dict(font=dict(size=10), x=1.05, y=0.5))
        st.plotly_chart(fig_mentor_exp, use_container_width=True)
    
    # Strengths and Note side-by-side at bottom
    col_strength, col_note = st.columns(2)
    
    with col_strength:
        st.markdown("""
        <div class="insight-box green">
          <strong>✓ Strengths:</strong> Most balanced network across sectors and experience levels. With 23% at 1–3 years and 26% at 3–5 years, mentors provide near-peer mentorship and relatable guidance. This counterbalances the seniority-heavy speaker and partner networks.
        </div>
        """, unsafe_allow_html=True)
    
    with col_note:
        st.markdown("""
        <div class="insight-box blue">
          <strong>ℹ Note:</strong> This network is well-distributed and serves as a strong counterweight to gaps in other roles. It successfully bridges the early-career perspective gap left by speaker and government partner networks.
        </div>
        """, unsafe_allow_html=True)

# ── KEY FINDINGS ──
st.markdown('<div id="key-findings"></div>', unsafe_allow_html=True)
with st.expander("🔍 Key Findings", expanded=True):
    findings = [
        ("blue",   "AI, Civic/Gov Tech & Public Policy are core strengths", "Consistent across all roles — reflecting Paragon's focus at the intersection of tech, governance, and policy."),
        ("orange", "Seniority defines the network", "72% of speakers and 74% of gov partners have 10+ years. Strong credibility, but a gap in early-career perspective."),
        ("green",  "The mentor network is most balanced", "Strongest distribution across sectors and experience levels. Counterweight to seniority concentration elsewhere."),
        ("blue",   "Government partners are locally concentrated", "67% in local government, creating strong community connections but limited state and federal representation."),
        ("orange", "AI is top across all three roles", "31% of speakers, 37% of mentors, 19% of gov partners — reflecting Paragon's identity in tech policy."),
        ("green",  "About Speaker Diversity (Research vs. Practitioner)", "Paragon's speaker network is well-aligned with core themes, with strong representation from both research and practitioner backgrounds."),
    ]
    for color, title, body in findings:
        st.markdown(f"""
        <div class="insight-box {color}">
          <strong>{title}</strong><br>
          <span style="font-size:0.85rem; color:#7a85a8;">{body}</span>
        </div>
        """, unsafe_allow_html=True)

# ── STRENGTHS & WEAKNESSES ──
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div id="strengths"></div>', unsafe_allow_html=True)
    with st.expander("✅ Network Strengths", expanded=True):
        strengths = [
            "Mentor network highly diversified across sectors and experience levels.",
            "72% speakers and 74% gov partners are 10+ year veterans — exceptional credibility.",
            "Strong identity in AI, Policy, and Civic/Gov Tech across all roles.",
            "Gov partner network especially strong in local government.",
            "Each role contributes distinct value to the ecosystem.",
        ]
        for s in strengths:
            st.markdown(f'<div class="insight-box green" style="font-size:0.85rem;">✓ {s}</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div id="weaknesses"></div>', unsafe_allow_html=True)
    with st.expander("⚠️ Network Weaknesses", expanded=True):
        weaknesses = [
            "Speaker network overwhelmingly senior — only 3% are 1–3 years experience.",
            "Limited presence in Healthcare, Cybersecurity, National Security, Legal, Media.",
            "Gap in mid-career representation across all roles.",
            "Early-career perspective mostly siloed in mentoring.",
        ]
        for w in weaknesses:
            st.markdown(f'<div class="insight-box orange" style="font-size:0.85rem;">⚠ {w}</div>', unsafe_allow_html=True)

# ── RECOMMENDATIONS ──
st.markdown('<div id="recommendations"></div>', unsafe_allow_html=True)
with st.expander("💡 Recommendations", expanded=True):
    recs = [
        ("1", "Expand early-career speakers", "Increase speakers in 1–3 and 3–5 year range. Mentor network is a natural pipeline."),
        ("2", "Seek underrepresented sectors intentionally", "Maintain AI/policy strength while broadening into Healthcare/Biotech, Media, National Security."),
        ("3", "Add mid-career professionals", "Bridge gap between senior experts and early-career mentors."),
        ("4", "Focus on 3–4 sectors per cohort", "Go deep on underrepresented areas rather than broad expansion."),
    ]
    for num, title, body in recs:
        st.markdown(f"""
        <div style="padding:1rem 1.25rem; margin-bottom:0.6rem; border: 0.5px solid #e0e0e0; border-radius: 8px;">
          <div style="display:flex; align-items:flex-start; gap:1rem;">
            <div style="font-family:Georgia, serif; font-size:2rem; color:#378ADD; line-height:1; min-width:2rem; text-shadow: 0 0 3px rgba(55,138,221,0.3);">{num}</div>
            <div>
              <strong>{title}</strong>
              <p style="font-size:0.85rem; margin-top:0.3rem; margin-bottom:0; opacity:0.85;">{body}</p>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── QUESTIONS FOR THE FUTURE ──
with st.expander("❓ Questions for the Future", expanded=False):
    st.markdown('<div style="color:#7a85a8; margin-bottom:1rem; font-size:0.9rem;">Paragon may consider these questions as it continues developing its network and fellowship models.</div>', unsafe_allow_html=True)
    
    questions = [
        "Does Paragon want each role to continue serving a distinct function, or aim for more balance across roles?",
        "How can Paragon better engage its alumni network as active members, speakers, mentors, and recruiters?",
        "Does Paragon want to maintain its strong local government focus, or expand to state and federal levels?",
        "Which sectors and industries should Paragon prioritize for future relationship building?",
        "As technology and regulation continue to evolve, which topics and connections will Paragon prioritize?",
        "How should Paragon balance research and practical implementation in network building?",
        "How can Paragon better track and balance technical vs. non-technical roles?",
        "What does success look like for the network over the next few years?",
    ]
    for q in questions:
        st.markdown(f'<div style="padding:0.75rem 1rem; margin-bottom:0.5rem; background-color:#f5f5f5; border-radius:6px; font-size:0.9rem; color:#1a1a1a;">❓ {q}</div>', unsafe_allow_html=True)