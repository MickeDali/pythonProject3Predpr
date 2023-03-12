from yattag import Doc



doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html', 'lang="ru"'):
    #text.asis('<link href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel = "stylesheet", integrity = "sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD", crossorigin = "anonymous" >')
    with tag('head'):
        with tag('meta charset="UTF-8"'):
            with tag('title'):
                text('Title')
    with tag('body'):
        text('Here is my variable: {{ variable }}')
    with tag('form', action="/get-text", method="POST"):
        doc.stag('input', name="in1", type="submit", value="Go!")
    with tag('table', width="400", border="5", cellspacing="0", cellpadding="5", bgcolor="white", bordercolor="blue"):
        with tag('tr'):
            with tag('th'):
                with tag('table', width="100%", border="5", cellspacing="4", cellpadding="5", bgcolor="lightblue", bordercolor="lightblue"):
                    with tag('tr', height="25", bgcolor="pink"):
                        text('data')
                        with tag('td', draggable="true"):
                            text('times')
                            with tag('p', style="text-align: right;"):
                                text('times1')
                                with tag('form', action=""):
                                    doc.stag('input', ame="save", type="submit", klass="submit", value="Сохранить")
                    with tag('tr', height="150"):
                        with tag('td'):
                            text('times2')
                            with tag('form', action="/get-text", type="text", method="POST"):
                                doc.stag('input', name="add1", type="submit", value="ADD")
                    with tag('tr', height="100", bgcolor="lightgreen"):
                        with tag('td'):
                            text('times3')
                            with tag('form', action="/get-text", type="text", method="POST"):
                                doc.stag('input', name="red1", type="submit", value="RED")
                            with tag('form', action="/get-text", type="text", method="POST"):
                                doc.stag('input', name="mov1", type="submit", value="MOV")
                            with tag('form', action="/get-text", type="text", method="POST"):
                                doc.stag('input', name="del1", type="submit", value="DEL")
                    with tag('tr', height="25"):
                        with tag('td'):
                            text('times4')


result = doc.getvalue()

f = open('templates/index.html', 'w')
f.write(result)
f.close()