# DevChatPro - Echtzeit-Kollaborations-Entwicklungstool

DevChatPro ist ein leistungsstarkes Echtzeit-Kollaborations-Entwicklungstool, das Entwicklern ermöglicht, effektiv zusammenzuarbeiten, Projekte zu verwalten und qualitativ hochwertigen Code zu erstellen.

## Projektüberblick

DevChatPro wurde entwickelt, um die Entwicklung von Softwareprojekten zu optimieren und Entwicklerteams bei der Zusammenarbeit und dem Projektmanagement zu unterstützen. Das Projekt wird schrittweise von einem MVP (Minimum Viable Product) zu einer vollständig erweiterten Anwendung entwickelt.

### Funktionen im Überblick

- **Grundlegende Chat-Funktionen:** 
  - Benutzerauthentifizierung
  - Chat-Raum erstellen
  - Echtzeit-Chat
  - Nachrichtenverlauf


- **Projektmanagement:**
  - Projekte erstellen
  - Projekte verwalten
  - Datei-Upload/Download

- **Dokumentation:**
  - Markdown-Editor
  - Dokumentation anzeigen

- **Docker-Integration:**
  - Docker-Container
  - Script-Ausführung

- **Erweiterte Funktionen:**
  - Code Collaboration
  - Versionskontrolle
  - Automatisierte Tests
  - Live-Code-Review
  - Projektmetriken und -statistiken
  - Berechtigungs- und Datenschutzsystem
  - Integration von Drittanbietern
  - Benutzeroberflächenverbesserungen
  - Schulung und Support
  - Überwachung und Skalierung

## Entwicklungsleitfaden

Um DevChatPro zu verwenden oder weiterzuentwickeln, folgen Sie diesem Entwicklungsleitfaden:

1. **Klonen Sie das Repository:**
   ```
   git clone https://github.com/IhrGitHubBenutzername/DevChatPro.git
   ```

2. **Installieren Sie die erforderlichen Abhängigkeiten:**
   ```
   pip install -r requirements.txt
   ```

3. **Starten Sie die Anwendung:**
   ```
   python src/main.py
   ```

4. **Zugriff auf die Anwendung:**
   Besuchen Sie `http://localhost:5000` in Ihrem Webbrowser.

## Mitwirkende

- [Ihr Name](https://github.com/IhrGitHubBenutzername)
- [Mitwirkender Name](https://github.com/mitwirkenderGitHubBenutzername)

Wenn Sie zu diesem Projekt beitragen möchten, lesen Sie bitte unsere [Mitwirkendenrichtlinien](CONTRIBUTING.md).

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert.

## Kontakt

Bei Fragen oder Feedback können Sie uns unter [Ihre E-Mail-Adresse](mailto:IhreE-Mail@Beispiel.com) erreichen.

---


```
DevChatPro
├─ .gitignore
├─ app
│  ├─ api
│  │  ├─ auth
│  │  │  ├─ auth_crypt.py
│  │  │  ├─ auth_models_schemas.py
│  │  │  ├─ auth_router.py
│  │  │  ├─ auth_schemas.py
│  │  │  ├─ auth_services.py
│  │  │  └─ __init__.py
│  │  ├─ chat
│  │  │  ├─ chat_models.py
│  │  │  ├─ chat_router.py
│  │  │  ├─ chat_services.py
│  │  │  ├─ chat_sockets.py
│  │  │  └─ __init__.py
│  │  ├─ documentation
│  │  │  ├─ documentation_models.py
│  │  │  ├─ documentation_router.py
│  │  │  ├─ documentation_services.py
│  │  │  ├─ documentation_utils.py
│  │  │  └─ __init__.py
│  │  └─ projects
│  │     ├─ projects_models.py
│  │     ├─ projects_router.py
│  │     ├─ projects_services.py
│  │     ├─ projects_tasks.py
│  │     └─ __init__.py
│  ├─ core
│  │  ├─ config.py
│  │  ├─ database.py
│  │  ├─ middleware.py
│  │  ├─ sqlite_database.db
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ static
│  │  ├─ css
│  │  │  └─ style.css
│  │  ├─ images
│  │  │  └─ logo.png
│  │  └─ js
│  │     └─ main.js
│  ├─ templates
│  │  ├─ chat_room.html
│  │  ├─ dashboard.html
│  │  ├─ documentation.html
│  │  ├─ index.html
│  │  └─ project_management.html
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ MVP-Guide.md
├─ poetry.lock
├─ pyproject.toml
├─ README.md
└─ tests
   ├─ test_auth.py
   ├─ test_chat.py
   ├─ test_documentation.py
   └─ test_projects.py

```
```
DevChatPro
├─ .env
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ fsmonitor--daemon
│  │  └─ cookies
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ main
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ 8f8cfc80d416610af191662fdd7cbf1da03c4a
│  │  ├─ 01
│  │  │  └─ e65fb1c4515fd6725e92d7d2176bc935bbe88b
│  │  ├─ 03
│  │  │  └─ bea976049c19fd5537845ecf8b5a8255428fe6
│  │  ├─ 06
│  │  │  └─ 6387494dfc448249293895631babd1e469530b
│  │  ├─ 07
│  │  │  └─ 433db73f2a7da9b26875bce593f23388dd99c1
│  │  ├─ 08
│  │  │  └─ 4bb58b46b2de0157c39d105754df6c5901b221
│  │  ├─ 10
│  │  │  └─ 9946a59dd49046e5a9b3574bd66fa051a756a8
│  │  ├─ 11
│  │  │  └─ be8956eb30317341940876a78b47898a73a06d
│  │  ├─ 13
│  │  │  └─ 608a8a71d014b5cfe99d8f31b0e073c3365aa2
│  │  ├─ 15
│  │  │  └─ 8751fd15fbd1c5e066459d89904fa5b58d7b17
│  │  ├─ 1e
│  │  │  └─ f7e2ae62147ba7d149521a4dd60c1e77169976
│  │  ├─ 1f
│  │  │  └─ d0cfaf707093d26ae55a9c5f1b42afa182e9a6
│  │  ├─ 22
│  │  │  └─ 5d5ba8ac3c873b74593742ec372ab5d265cbd7
│  │  ├─ 23
│  │  │  └─ 75708158f56367adbd7cb69c1d3297d5daeff5
│  │  ├─ 25
│  │  │  └─ 9a033b6eef0b8880746557f158167e64c3fb53
│  │  ├─ 29
│  │  │  ├─ 1de6eef45802784c73674906356253820d2538
│  │  │  └─ 9fe3b8f7e9d04f710cf6163a3aeec6ea118238
│  │  ├─ 2b
│  │  │  └─ 5a0dbaad5c858f3b4aa7afebe40a8171e380c6
│  │  ├─ 31
│  │  │  └─ 0ecd90a8b01b99b2eb48a756d5e1094f365a13
│  │  ├─ 33
│  │  │  ├─ 3279af0dd1cc71e94f9a79743eb25f1d39e3a9
│  │  │  └─ ee87163e0f1807e5d9e66e7c83fdf5b524fca7
│  │  ├─ 37
│  │  │  └─ e364c18e761107682b3daf3356300988ef5d09
│  │  ├─ 42
│  │  │  └─ c8e10deade4e51beeeccda268b0577c05b8757
│  │  ├─ 45
│  │  │  └─ d83d3c171e05f1d01a9e5fcccd49e0391d4975
│  │  ├─ 47
│  │  │  └─ 2ddb5e8959587623c760a090aa8ac24cc2bacc
│  │  ├─ 49
│  │  │  └─ 290d4c42b67663ce0fa7e2a3daa0951a07b36c
│  │  ├─ 4b
│  │  │  └─ 60e0f0d78795f00c194f86b465ef8167df3aea
│  │  ├─ 50
│  │  │  └─ 855df3be22dc6bd0df5646c12c02516975e403
│  │  ├─ 5a
│  │  │  ├─ 05a70f11c32e73a9558569a981930fb62ea07e
│  │  │  └─ 9d80349aade6f0507110cbec61f71c29446378
│  │  ├─ 5c
│  │  │  └─ ea76d8b0b44eec799db41b24052207005ec1b0
│  │  ├─ 5d
│  │  │  └─ 1149069b2c7b907549c323f45d86a96786c6b0
│  │  ├─ 61
│  │  │  └─ d9bb0c5fff9443f8bf0047554da220a6bb99f1
│  │  ├─ 62
│  │  │  └─ 557424d1b09191260e2bdc278a3f63bd9cbf4e
│  │  ├─ 66
│  │  │  └─ 6de13571aef88f00b35c744da750ef4723c4ea
│  │  ├─ 67
│  │  │  └─ cec002c8b60667055733a1043b2f6e4d617eb5
│  │  ├─ 6b
│  │  │  └─ 82e6c1ccb3de0693bbad6c87c9835320fbc6d4
│  │  ├─ 6f
│  │  │  └─ 3a06abe40d42e33ffc3b601708d4876ee8c67f
│  │  ├─ 75
│  │  │  └─ d36dad7fb389452ff8f12c6a7a8cd90ac2933e
│  │  ├─ 77
│  │  │  └─ 8768aa2df375302d04f4137db3d516fb3ae454
│  │  ├─ 7c
│  │  │  └─ 25ff8875d11590a6ff3a3f4565d2abc44a4cf5
│  │  ├─ 7f
│  │  │  ├─ 55342c36c8fbeafef00410c7e4825f9cb7c46a
│  │  │  └─ c278a67f9ea7def740ae6fd9150f5a7918747d
│  │  ├─ 86
│  │  │  └─ d3f7d934c84ad73216eabb9e08d71edddb3ce5
│  │  ├─ 8a
│  │  │  └─ a80c28ec0bf96d936ee75c7506bd2505acc3b6
│  │  ├─ 8b
│  │  │  └─ 6dd67a5de063b2a73283c39ad21a0683834df2
│  │  ├─ 9d
│  │  │  └─ 765e59acb0f3999bd1ce384918534134dfe173
│  │  ├─ 9e
│  │  │  └─ 7d8fe395ccc6a7411f677b36bfd42f9f22692b
│  │  ├─ a1
│  │  │  └─ 1936596827675d36871e18349d4f174b01af8e
│  │  ├─ a2
│  │  │  └─ b037bca6ceab07ecffe39dfba47dd847e66155
│  │  ├─ ac
│  │  │  └─ 01c845dfeea113b29c3cc11948fe26fd894ebb
│  │  ├─ ad
│  │  │  ├─ 37dd5f3b6141dd2067d66d527d9c7a7ff99f00
│  │  │  └─ bcf062c3653be3b80a088170fe35a4b98c4370
│  │  ├─ ae
│  │  │  └─ 893e59a541728e4f06f63c8c2ecf8abb8bd4d1
│  │  ├─ af
│  │  │  └─ 0a9821b66c7ee85751f6a88d8600feb762a5c0
│  │  ├─ b1
│  │  │  └─ c02fd004fc706ed29f9854e92e4344149ff508
│  │  ├─ b7
│  │  │  └─ 76f303bba9dc8ed4305a25a1f9b7bd93e033e0
│  │  ├─ b9
│  │  │  └─ d4be4f028dda16648c644f83b389a3023d1351
│  │  ├─ bb
│  │  │  ├─ 147a05f89b11c9da69c2529df74aafd53ba4a8
│  │  │  └─ 55738eaf2c42a7f2c2d64f38e79e7b45491220
│  │  ├─ bc
│  │  │  └─ 2aeb08ec2cff4fd41a19920fb2570d237f5e35
│  │  ├─ c1
│  │  │  ├─ 664823cd431475d2c7de3481255a0d99b66b34
│  │  │  └─ 6c22b577f016121da8ec826ec93cc01226ce6d
│  │  ├─ c3
│  │  │  └─ 8af3f60f06143f41c50c5565e7d34946c19b91
│  │  ├─ c7
│  │  │  └─ bbe8e3400d140f47aee810a9fd5886d4587bfa
│  │  ├─ ca
│  │  │  └─ c9db31b081c08b82c427a978d19c1c4471f0e8
│  │  ├─ cb
│  │  │  ├─ 0c8502dc28b5ea30a1bd7c3736c34aa4af5bf0
│  │  │  └─ 3121c39d583b952b7f2e05e474fa3bbb9fb668
│  │  ├─ cc
│  │  │  └─ fa5d6212dd986fc5bc213ef15ec92c9a00621c
│  │  ├─ cf
│  │  │  └─ 30ac8c1b43783c72d1c522f1a99daf51951632
│  │  ├─ d4
│  │  │  └─ 60001fe11362884394a9574b93c1552c3e61fb
│  │  ├─ d9
│  │  │  └─ 005f2cc7fc4e65f14ed5518276007c08cf2fd0
│  │  ├─ de
│  │  │  └─ 788725ecf9efe6c907995f50d73074790b5c08
│  │  ├─ df
│  │  │  └─ e0770424b2a19faf507a501ebfc23be8f54e7b
│  │  ├─ e4
│  │  │  └─ 233f26b62bb359a7119413d271b5e517b1cb8e
│  │  ├─ e6
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ ee
│  │  │  └─ 461438425299d58e61265708f87e7b84e10603
│  │  ├─ f6
│  │  │  ├─ 0c0ce6faab766d0c7e9277fa25090adbc794db
│  │  │  └─ d37089d6e1ca4cf4c8efd0dfdafdb6485d3cd1
│  │  ├─ f7
│  │  │  └─ 62b173672476c1f98f410bf8d10484044870f7
│  │  ├─ fa
│  │  │  └─ a650592182f7826d47114bc5e65de5dfeeeed6
│  │  ├─ ff
│  │  │  └─ 531cf16f79b70d20baa10c4e70ac3371fcde7b
│  │  ├─ info
│  │  └─ pack
│  ├─ ORIG_HEAD
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ main
│     └─ tags
├─ .gitattributes
├─ .gitignore
├─ app
│  ├─ api
│  │  └─ auth
│  │     ├─ auth_models_schemas.py
│  │     ├─ cryptographie.py
│  │     ├─ services.py
│  │     ├─ tokens.py
│  │     └─ __init__.py
│  ├─ core
│  │  ├─ config.py
│  │  ├─ database.py
│  │  ├─ exceptions.py
│  │  ├─ middleware.py
│  │  ├─ sqlite_database.db
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ static
│  │  ├─ css
│  │  │  └─ style.css
│  │  ├─ images
│  │  │  ├─ cover.png
│  │  │  ├─ default.png
│  │  │  ├─ info.txt
│  │  │  ├─ profile.png
│  │  │  └─ vector
│  │  │     ├─ default-monochrome-black.svg
│  │  │     ├─ default-monochrome-white.svg
│  │  │     ├─ default-monochrome.svg
│  │  │     ├─ default.svg
│  │  │     ├─ isolated-layout.svg
│  │  │     ├─ isolated-monochrome-black.svg
│  │  │     └─ isolated-monochrome-white.svg
│  │  └─ js
│  │     └─ main.js
│  ├─ templates
│  │  ├─ auth
│  │  │  ├─ login.html
│  │  │  └─ test.html
│  │  ├─ base.html
│  │  ├─ dashboard.html
│  │  ├─ index.html
│  │  └─ project_management.html
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ LICENSE
├─ MVP-Guide.md
├─ poetry.lock
├─ pyproject.toml
└─ README.md

```