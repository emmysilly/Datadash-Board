# ─── PAGE: NETWORK ANALYSIS REPORT ───────────────────────────
elif page == "📄 Network Analysis Report":
    st.markdown("# Network Analysis Report")
    st.markdown('<div style="color:#7a85a8; margin-bottom:1.5rem; font-size:0.9rem;">Paragon Network · Spring 2026 · Strategic analysis of speakers, government partners, and mentors.</div>', unsafe_allow_html=True)

    # Quick-nav pills
    st.markdown("""
    <div style="margin-bottom:1.5rem;">
      <span class="pill pill-blue">Overall Network</span>
      <span class="pill pill-blue">Speakers</span>
      <span class="pill pill-blue">Gov Partners</span>
      <span class="pill pill-blue">Mentors</span>
      <span class="pill pill-orange">Strengths</span>
      <span class="pill pill-orange">Weaknesses</span>
      <span class="pill pill-green">Recommendations</span>
    </div>
    """, unsafe_allow_html=True)

    # ── OVERALL NETWORK ──
    with st.expander("🌐 Overall Network", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="report-section">
              <h3>Overview</h3>
              <p>Paragon's evolving network is a core part of the organization — shaping who fellows learn from, the kinds of projects and partnerships that are possible, and which professional pathways are most visible and accessible.</p>
              <p>This report analyzes Paragon's existing network as of Spring 2026 to identify patterns, strengths, gaps, and opportunities for growth.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            # Industry breakdown donut
            industries = ["Gov Partners", "Private", "AI", "Public Policy", "Nonprofit/Advocacy", "Research & Academia", "Other"]
            pcts = [32, 14, 11, 9, 9, 9, 16]
            fig = go.Figure(go.Pie(
                labels=industries, values=pcts, hole=0.55,
                marker_colors=[C_BLUE, C_ORANGE, C_GREEN, C_PURPLE, "#ff5b8c", "#ffb85b", C_BORDER],
                textinfo="percent",
                textfont=dict(size=11, color="white"),
                hovertemplate="%{label}: %{value}%<extra></extra>",
            ))
            fig.update_layout(**PLOTLY_LAYOUT, height=260, showlegend=True,
                legend=dict(font=dict(color=C_MUTED, size=10), orientation="v", x=1))
            st.plotly_chart(fig, use_container_width=True)

        # Sector chart
        sectors = ["AI", "Civic/Gov Tech", "Public Policy", "Data & Analytics", "Legal", "Cybersecurity", "National Security", "Other"]
        sector_pcts = [19, 17, 12, 8, 7, 6, 5, 26]
        fig_sec = go.Figure(go.Bar(
            x=sectors, y=sector_pcts,
            marker_color=[C_BLUE, C_GREEN, C_ORANGE, C_PURPLE, "#ff5b8c", "#ffb85b", "#5bffff", C_BORDER],
            marker_line_width=0,
            text=[f"{p}%" for p in sector_pcts],
            textposition="outside",
            textfont=dict(color=C_MUTED, size=11),
        ))
        fig_sec.update_layout(
            **PLOTLY_LAYOUT, height=260,
            title=dict(text="Network by Sector", font=dict(color=C_MUTED, size=13)),
            xaxis=dict(tickfont=dict(color=C_TEXT, size=11)),
            yaxis=dict(tickfont=dict(color=C_MUTED), gridcolor=C_BORDER, ticksuffix="%"),
        )
        st.plotly_chart(fig_sec, use_container_width=True)

    # ── SPEAKERS ──
    with st.expander("🎤 Speakers", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="report-section">
              <h3>Speaker Network</h3>
              <p>By sector, speakers are relatively diversified — strongest in <strong>Research & Academia (28%)</strong>, <strong>Private (22%)</strong>, and <strong>Nonprofit/Advocacy (16%)</strong>. Combined government representation sits at 18%.</p>
              <p>By industry, AI (31%), Public Policy (25%), and Civic/Gov Tech (16%) lead. After that, representation drops off significantly — Legal and Data & Analytics each at 9%, while Cybersecurity, National Security, and Media/Communications are at 3%.</p>
              <p><strong>Experience gap:</strong> 72% of speakers have 10+ years of experience. Only 3% are in the 1–3 year range, and 6% in the 3–5 year range — creating a gap in early-career perspective.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            # Speaker industry chart
            sp_industries = ["AI", "Public Policy", "Civic/Gov Tech", "Legal", "Data & Analytics", "Cybersecurity", "Nat. Security", "Media/Comms"]
            sp_pcts = [31, 25, 16, 9, 9, 3, 3, 3]
            fig = go.Figure(go.Bar(
                y=sp_industries, x=sp_pcts, orientation="h",
                marker_color=C_BLUE, marker_line_width=0,
                text=[f"{p}%" for p in sp_pcts], textposition="outside",
                textfont=dict(color=C_MUTED, size=11),
            ))
            fig.update_layout(**PLOTLY_LAYOUT, height=280,
                title=dict(text="Speakers by Industry", font=dict(color=C_MUTED, size=12)),
                xaxis=dict(showticklabels=False, showgrid=False),
                yaxis=dict(tickfont=dict(color=C_MUTED), autorange="reversed"),
            )
            st.plotly_chart(fig, use_container_width=True)

        # Experience breakdown
        exp_labels = ["10+ years", "5–9 years", "3–5 years", "1–3 years"]
        exp_speaker = [72, 19, 6, 3]
        exp_mentor  = [31, 20, 26, 23]
        exp_govpart = [74, 15, 7, 4]
        fig_exp = go.Figure()
        for label, vals, color in [("Speakers", exp_speaker, C_BLUE), ("Mentors", exp_mentor, C_GREEN), ("Gov Partners", exp_govpart, C_ORANGE)]:
            fig_exp.add_trace(go.Bar(name=label, x=exp_labels, y=vals, marker_color=color, marker_line_width=0))
        fig_exp.update_layout(
            **PLOTLY_LAYOUT, barmode="group", height=260,
            title=dict(text="Experience Distribution by Role", font=dict(color=C_MUTED, size=12)),
            legend=dict(font=dict(color=C_MUTED), orientation="h", y=-0.2),
            xaxis=dict(tickfont=dict(color=C_TEXT)),
            yaxis=dict(tickfont=dict(color=C_MUTED), gridcolor=C_BORDER, ticksuffix="%"),
        )
        st.plotly_chart(fig_exp, use_container_width=True)

    # ── GOVERNMENT PARTNERS ──
    with st.expander("🏛️ Government Partners", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="report-section">
              <h3>Government Partner Network</h3>
              <p>The government partner network is concentrated primarily in <strong>local government (67%)</strong>, followed by state (19%) and federal (4%). A smaller share has transitioned into Nonprofit/Advocacy (7%) and Private (4%).</p>
              <p>This reflects Paragon's strength in working on projects close to implementation and community-level governance. However, the network is less connected to state and federal government institutions.</p>
              <p>By industry, <strong>Civic/Gov Tech (37%)</strong> leads, followed by AI (19%) and Public Policy (15%). 74% of government partners have 10+ years of experience.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            # Gov sector pie
            gov_sectors = ["Local Gov", "State Gov", "Federal Gov", "Nonprofit/Advocacy", "Private"]
            gov_pcts = [67, 19, 4, 7, 4]
            fig = go.Figure(go.Pie(
                labels=gov_sectors, values=gov_pcts, hole=0.5,
                marker_colors=[C_BLUE, C_GREEN, C_ORANGE, C_PURPLE, "#ffb85b"],
                textinfo="percent+label",
                textfont=dict(size=10, color="white"),
            ))
            fig.update_layout(**PLOTLY_LAYOUT, height=260, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    # ── MENTORS ──
    with st.expander("🤝 Mentors", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="report-section">
              <h3>Mentor Network</h3>
              <p>The mentor network is the most balanced across sectors: <strong>Private (34%)</strong>, Research & Academia (23%), Nonprofit/Advocacy (17%), Federal Government (14%).</p>
              <p>By industry, AI (37%), Public Policy (20%), and Civic/Gov Tech (17%) lead, followed by Legal (11%), Cybersecurity (9%), and Energy (6%).</p>
              <p>Unlike speakers and government partners, mentors show the <strong>greatest variety in experience levels</strong>: 10+ years (31%), 3–5 years (26%), 1–3 years (23%), 5–9 years (20%). This makes the mentor network a counterweight to the seniority-heavy speaker pool.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            mentor_sectors = ["Private", "Research & Academia", "Nonprofit/Advocacy", "Federal Gov", "Other"]
            mentor_pcts = [34, 23, 17, 14, 12]
            fig = go.Figure(go.Pie(
                labels=mentor_sectors, values=mentor_pcts, hole=0.5,
                marker_colors=[C_ORANGE, C_BLUE, C_GREEN, C_PURPLE, C_BORDER],
                textinfo="percent",
                textfont=dict(size=11, color="white"),
            ))
            fig.update_layout(**PLOTLY_LAYOUT, height=260, showlegend=True,
                legend=dict(font=dict(color=C_MUTED, size=10)))
            st.plotly_chart(fig, use_container_width=True)

    # ── KEY FINDINGS ──
    with st.expander("🔍 Key Findings", expanded=True):
        findings = [
            ("blue",   "AI, Civic/Gov Tech & Public Policy are the network's core strengths", "Consistent across speakers, government partners, and mentors — reflecting Paragon's work at the intersection of technology, governance, and policy."),
            ("orange", "Seniority defines the network", "72% of speakers and 74% of gov partners have 10+ years of experience. Strong authority and credibility, but a gap in early-career perspective that the mentor network partially addresses."),
            ("green",  "The mentor network is the most balanced", "Strongest sector, industry, and experience distribution of all three network roles. Provides a counterweight to the seniority concentration elsewhere."),
            ("blue",   "Government partners are locally concentrated", "67% are in local government, creating strong community-level connections but limited state and federal representation."),
            ("orange", "AI is the top industry across all three roles", "31% of speakers, 37% of mentors, and 19% of gov partners work in AI — reflecting Paragon's central identity in the tech policy space."),
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
        with st.expander("✅ Network Strengths", expanded=True):
            strengths = [
                "Mentor network is highly diversified across sectors and experience levels — strong mentor-mentee matching potential.",
                "72% of speakers and 74% of gov partners are 10+ year veterans — exceptional credibility and depth of knowledge.",
                "Strong identity: clearly focused in AI, Policy, and Civic/Gov Tech across all roles.",
                "Gov partner network is especially strong in local government — close to implementation and community-level impact.",
                "Each role contributes distinct value: speakers (senior insight), gov partners (local connections), mentors (diverse guidance).",
            ]
            for s in strengths:
                st.markdown(f'<div class="insight-box green" style="font-size:0.85rem;">✓ {s}</div>', unsafe_allow_html=True)

    with col2:
        with st.expander("⚠️ Network Weaknesses", expanded=True):
            weaknesses = [
                "Speaker network is overwhelmingly senior (only 3% are 1–3 years experience) — risks feeling aspirational rather than accessible.",
                "Limited presence in Healthcare/Biotech, Cybersecurity, National Security, Legal, Think Tank, Philanthropic, and Media/Communications.",
                "Gap in mid-career representation across all roles — missing voices that are relatable but grounded.",
                "Early-career perspective exists but is mostly siloed in mentoring — limited reach compared to speaker programming.",
            ]
            for w in weaknesses:
                st.markdown(f'<div class="insight-box orange" style="font-size:0.85rem;">⚠ {w}</div>', unsafe_allow_html=True)

    # ── RECOMMENDATIONS ──
    with st.expander("💡 Recommendations", expanded=True):
        recs = [
            ("1", "Expand early-career speakers", "Increase the number of speakers in the 1–3 and 3–5 year experience range. The mentor network is a natural pipeline — leverage it for future speaker nominations."),
            ("2", "Seek underrepresented sectors intentionally", "Maintain AI/policy strength while broadening into Healthcare/Biotech, Media, National Security, and Think Tanks to widen career pathways."),
            ("3", "Add mid-career professionals", "Bridge the gap between senior experts and early-career mentors. Mid-career voices are relatable and practically grounded."),
            ("4", "Focus on 3–4 sectors per cohort", "Rather than broad expansion, go deep on 3–4 underrepresented areas at a time — enabling stronger representation and more thoughtful programming."),
        ]
        for num, title, body in recs:
            st.markdown(f"""
            <div class="report-section" style="padding:1rem 1.25rem; margin-bottom:0.6rem;">
              <div style="display:flex; align-items:flex-start; gap:1rem;">
                <div style="font-family:'DM Serif Display',serif; font-size:2rem; color:{C_BLUE}; line-height:1; min-width:2rem;">{num}</div>
                <div>
                  <strong style="color:{C_TEXT};">{title}</strong>
                  <p style="font-size:0.85rem; color:{C_MUTED}; margin-top:0.3rem; margin-bottom:0;">{body}</p>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    # ── FUTURE QUESTIONS ──
    with st.expander("🔭 Questions for the Future", expanded=False):
        questions = [
            "Does Paragon want each role to continue serving a distinct function, or aim for more balance across roles?",
            "How can Paragon better engage its alumni network as active connectors, speakers, mentors, and recruiters?",
            "Should Paragon maintain its strong local government focus, or expand state and federal relationships?",
            "Which sectors and industries should Paragon prioritize for future relationship building?",
            "As technology and regulation evolve, which topics and connections will Paragon prioritize?",
            "How should Paragon balance research and practical implementation in network building and programming?",
            "How can Paragon better track and balance technical vs. non-technical roles in the network?",
            "What does network success look like in 2–3 years — larger, more balanced, more specialized, or all three?",
        ]
        for q in questions:
            st.markdown(f'<div class="insight-box blue" style="font-size:0.85rem;">❓ {q}</div>', unsafe_allow_html=True)

