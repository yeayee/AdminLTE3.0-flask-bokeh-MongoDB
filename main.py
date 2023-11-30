from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

app = Flask(__name__)

# 绘图，https://zhuanlan.zhihu.com/p/29576732

fig = figure(plot_width=500, plot_height=500)
fig.vbar(
        x=[1, 2, 3, 4],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 3.9],
        color='navy')
script,div = components(fig)
js_resources = INLINE.render_js()  # 基本图形比较简单js和css通用
css_resources = INLINE.render_css()



@app.route('/')
def bokeh():
    return render_template('index.html',
                    plot_script=script,
                    plot_div=div,
                    js_resources=js_resources,
                    css_resources=css_resources,
                )

@app.route('/adminlte')
def adminlte():
    x = [1, 2, 3, 4, 5]
    y = [4, 5, 5, 7, 2]
    p = figure(
        title="Toolbar autohide example",
        plot_width=500, plot_height=500
    )
    p.toolbar.autohide = True
    p.toolbar.logo = None  # Nice
    p.line(x, y)
    script2,div2 = components(p)
    return render_template('adminlte.html',
                    plot_script=script,
                    plot_div=div,
                    js_resources=js_resources,
                    css_resources=css_resources,
                    plot_script2=script2,
                    plot_div2=div2,
                )

# 非蓝图，简化展示recover-password
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/recover-password')
def recover_password():
    return render_template('recover-password.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/404')
def e404():
    return render_template('404.html')


@app.route('/500')
def e500():
    return render_template('500.html')


if __name__ == '__main__':
    app.run(debug=True)