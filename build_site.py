from pathlib import Path
from textwrap import dedent

SITE = {
    "name": "Sarfaraz Ahmed",
    "email": "space.sarfaraz216@gmail.com",
    "phone": "+92-319-4503446",
    "location": "Sindh, Pakistan",
    "tagline": "Prospective PhD Student — Intelligent, Secure & Sustainable Computing Systems",
    "about": "My research focuses on the development of intelligent, secure, and sustainable computing systems for reliable and high-performance digital infrastructures.",
    "research_interests": [
        "Systems & Application Security",
        "Advanced Networking and Data Security",
        "Intelligent and Sustainable Computing Systems",
        "Security & Privacy in Distributed Environments"
    ],
    "education": [
        {"when":"Feb 2026", "title":"BS Computer Science (CGPA: 3.72/4)", "where":"University of the People, USA", "extra":"Major: Systems & Application Security, Advanced Networking and Data Security"},
        {"when":"Aug 2022", "title":"HSC Pre-Engineering (Grade: A1)", "where":"Government Degree College, Thul", "extra":"Major: Mathematics, Physics, Chemistry"}
    ],
    "experience": [
        {"when":"Jul 2025 – Sep 2025", "title":"DevOps Intern", "where":"Software Productivity Strategists, Inc. (SPS), NSTP Islamabad", "detail":"Automation, CI/CD, containerized systems; Linux, cloud infrastructure, build pipelines."},
        {"when":"Jun 2025 – Jul 2025", "title":"Research Trainee", "where":"National University of Science and Technology (NUST), Pakistan", "detail":"Applied ML/DL; built models with Python, TensorFlow, Scikit-learn for intelligent data systems."}
    ],
    "publications": [
        {"when":"2025", "title":"Bridging the Gap: Aligning Physical and Cybersecurity in a Hybrid Threat Environment", "venue":"PIFFERS Security Services — Creative Writing Competition #007", "note":"Recognized for outstanding contribution in hybrid cybersecurity"}
    ],
    "awards": [
        {"when":"2025", "title":"Dean’s List 2024–2025", "where":"University of the People, USA"},
        {"when":"2023", "title":"President’s List 2023", "where":"University of the People, USA"},
        {"when":"Apr 2024", "title":"Aspire Leaders Program (Global Leadership)", "where":"Harvard Business School, USA"}
    ],
    "training": [
        {"when":"Apr–Jun 2025", "title":"CS106A Programming Methodologies", "where":"Stanford — Code in Place"},
        {"when":"Jan–Mar 2025", "title":"Introduction to Kubernetes (LFS158)", "where":"Linux Foundation"},
        {"when":"Jul–Nov 2024", "title":"IBM Cloud Essentials", "where":"edX"},
        {"when":"May–Jul 2024", "title":"Data Science Foundations", "where":"Google on Coursera"},
        {"when":"In Progress", "title":"Machine Learning", "where":"Andrew Ng — Coursera"},
        {"when":"In Progress", "title":"Distributed Systems (6.824)", "where":"MIT OpenCourseWare"},
        {"when":"In Progress", "title":"Web Development Bootcamp", "where":"Udemy"},
        {"when":"In Progress", "title":"Java Network Programming", "where":"Udemy"}
    ],
    "community": [
        {"when":"2024–Present", "title":"Community Leader (Pakistan)", "where":"Aspire Institute — Harvard University"},
        {"when":"2023–Present", "title":"Volunteer", "where":"International Humanitarian Aid Association (IHAA), Turkey"}
    ],
    "skills": [
        {"group":"Programming", "items":["C++","Python","MATLAB","SQL","JavaScript","HTML","CSS","PHP","Go","Java","Bash","C"]},
        {"group":"Machine Learning & Data", "items":["TensorFlow","NumPy","Pandas","Scikit-learn","MATLAB Toolboxes"]},
        {"group":"DevOps & Systems", "items":["Linux/Unix","GitHub","CI/CD","Shell Scripting","API Integration"]},
        {"group":"Research Tools", "items":["LaTeX","Jupyter Notebook","Overleaf","MATLAB Simulink","Visualization Tools"]},
        {"group":"Languages", "items":["English (Advanced)","Urdu (Advanced)","Sindhi (Native)"]}
    ]
}

CSS = dedent(""":root{
  --ink:#111; --muted:#5f6368; --line:#e5e7eb; --brand:#0b6efd;
  --head-bg:#000; --head-fg:#fff; --card-bg:#fff; --page-bg:#fff;
}
*{box-sizing:border-box} html,body{height:100%} html{scroll-behavior:smooth}
body{margin:0; background:var(--page-bg); color:var(--ink);
     font: 500 15px/1.55 Inter,system-ui,-apple-system,Segoe UI,Roboto,Arial;}
a{color:var(--brand); text-decoration:none} a:hover{text-decoration:underline}
/* Left-aligned page, high information density */
.wrap{max-width:1200px; margin-left:18px; margin-right:0; padding:18px}
.grid{display:grid; grid-template-columns:340px 1fr; gap:18px}
@media (max-width:1000px){ .grid{grid-template-columns:1fr} .left{position:relative !important} }
.left{position:sticky; top:16px; align-self:start}
.card{background:var(--card-bg); border:1px solid var(--line); border-radius:10px}
.profile{padding:12px}
.head{display:grid; grid-template-columns:64px 1fr; gap:10px; align-items:center}
.avatar{width:64px;height:64px;border-radius:10px;background:#f3f4f6;border:1px solid var(--line);display:grid;place-items:center;overflow:hidden}
.tagline{color:var(--muted); font-weight:600; margin-top:2px}
.meta{margin-top:8px; color:var(--muted)} .meta div{margin:4px 0}
.toc{margin-top:10px; padding:8px; border-top:1px solid var(--line); border-bottom:1px solid var(--line); border-radius:8px; background:#fafafa}
.toc a{display:block; padding:6px 8px; border-radius:6px; color:#333}
.toc a:hover{background:#eef2ff; text-decoration:none}
/* Sections */
section{border:1px solid var(--line); border-radius:10px; overflow:hidden; background:#fff; margin-bottom:12px}
summary{list-style:none; cursor:pointer; padding:10px 12px; background:var(--head-bg); color:var(--head-fg); user-select:none}
summary::-webkit-details-marker{display:none}
.title{font-weight:700; letter-spacing:.2px}
.body{padding:10px 12px; color:#111} /* body text black */
.item{display:grid; grid-template-columns:120px 1fr; gap:10px; padding:6px 0}
.when{color:#555; font-size:12px; padding-top:2px}
.what{display:flex; flex-direction:column; gap:2px}
.muted{color:var(--muted)}
.cols-2{display:grid; grid-template-columns:repeat(2,1fr); gap:10px}
.cols-3{display:grid; grid-template-columns:repeat(3,1fr); gap:10px}
@media (max-width:1000px){ .cols-2{grid-template-columns:1fr} .cols-3{grid-template-columns:1fr 1fr} }
@media (max-width:640px){ .cols-3{grid-template-columns:1fr} .item{grid-template-columns:1fr} }
footer{margin:16px 0 6px; color:#666; font-size:13px}
""")

def bullets(items):
    return "<ul>" + "".join(f"<li>{t}</li>" for t in items) + "</ul>"

def section_summary(title, anchor):
    return f'<summary id="{anchor}" class="title">{title}</summary>'

def section_block(title, anchor, inner_html):
    return f'<section><details open>{section_summary(title, anchor)}<div class="body">{inner_html}</div></details></section>'

def edu_html(rows):
    html = []
    for e in rows:
        html.append(
            f'<div class="item">'
            f'<div class="when">{e.get("when","")}</div>'
            f'<div class="what">'
            f'<div class="title">{e.get("title","")}</div>'
            f'<div class="muted">{e.get("where","")}</div>'
            f'<div class="muted">{e.get("extra","")}</div>'
            f'</div></div>'
        )
    return "".join(html)

def exp_html(rows):
    html = []
    for r in rows:
        html.append(
            f'<div class="item">'
            f'<div class="when">{r.get("when","")}</div>'
            f'<div class="what">'
            f'<div class="title">{r.get("title","")}</div>'
            f'<div class="muted">{r.get("where","")}</div>'
            f'<div class="muted">{r.get("detail","")}</div>'
            f'</div></div>'
        )
    return "".join(html)

def generic_list(rows):
    html = []
    for r in rows:
        html.append(
            f'<div class="item">'
            f'<div class="when">{r.get("when","")}</div>'
            f'<div class="what">'
            f'<div class="title">{r.get("title","")}</div>'
            f'<div class="muted">{r.get("where","")}</div>'
            f'</div></div>'
        )
    return "".join(html)

def skills_html(groups):
    cols = []
    for g in groups:
        cols.append(
            f'<div class="card" style="border:none">'
            f'<div class="title">{g["group"]}</div>'
            f'<div class="muted">{", ".join(g["items"])}</div>'
            f'</div>'
        )
    return f'<div class="cols-3">{"".join(cols)}</div>'

def render_html():
    left = (
        '<aside class="left card profile">'
        '<div class="head">'
        '<div class="avatar" aria-hidden="true">'
        '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#0b6efd" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M6 20a6 6 0 0 1 12 0"/></svg>'
        '</div>'
        '<div><div class="title">' + SITE["tagline"] + '</div></div>'
        '</div>'
        '<div class="meta">'
        f'<div><strong>Email:</strong> <a href="mailto:{SITE["email"]}">{SITE["email"]}</a></div>'
        f'<div><strong>Phone:</strong> {SITE["phone"]}</div>'
        f'<div><strong>Location:</strong> {SITE["location"]}</div>'
        '</div>'
        '<div class="toc">'
        '<a href="#research">Research Interest</a>'
        '<a href="#education">Education</a>'
        '<a href="#experience">Experience</a>'
        '<a href="#publications">Publications & Writing</a>'
        '<a href="#awards">Honors & Awards</a>'
        '<a href="#training">Professional Development & Training</a>'
        '<a href="#community">Community Service</a>'
        '<a href="#skills">Skills</a>'
        '<a href="#contact">Contact</a>'
        '</div>'
        '</aside>'
    )

    pubs_html = ""
    for p in SITE["publications"]:
        pubs_html += (
            '<div class="item"><div class="when">' + p["when"] + '</div>'
            '<div class="what"><div class="title">' + p["title"] + '</div>'
            '<div class="muted">' + p["venue"] + '</div><div class="muted">' + p["note"] + '</div></div></div>'
        )

    right = ""
    right += section_block("Research Interest", "research", '<p class="muted">' + SITE["about"] + '</p>' + bullets(SITE["research_interests"]))
    right += section_block("Education", "education", edu_html(SITE["education"]))
    right += section_block("Experience", "experience", exp_html(SITE["experience"]))
    right += section_block("Publications & Writing", "publications", pubs_html)
    right += section_block("Honors & Awards", "awards", generic_list(SITE["awards"]))
    right += section_block("Professional Development & Training", "training", generic_list(SITE["training"]))
    right += section_block("Community Service", "community", generic_list(SITE["community"]))
    right += section_block("Skills", "skills", skills_html(SITE["skills"]))
    contact = ('<p><strong>Email:</strong> <a href="mailto:' + SITE["email"] + '">' + SITE["email"] + '</a><br>'
               '<strong>Phone:</strong> ' + SITE["phone"] + '<br>'
               '<strong>Location:</strong> ' + SITE["location"] + '</p>')
    right += section_block("Contact", "contact", contact)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>PhD Portfolio — {SITE["name"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
  <div class="wrap">
    <div class="grid">
      {left}
      <main class="right">{right}
        <footer>© 2025 {SITE["name"]}</footer>
      </main>
    </div>
  </div>
</body>
</html>"""
    return html

def build(path="index.html"):
    Path(path).write_text(render_html(), encoding="utf-8")
    return Path(path).resolve()

if __name__ == "__main__":
    print("Writing index.html ...")
    out = build()
    print("Wrote:", out)
