from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def cgpa_calculator():
    if request.method=="POST":
        try:
            sem_count=int(request.form.get("semesterCount"))
        except:
            return "<h3> Inavalid Semester Count </h3>"
        sgpas = []
        for i in range(1, sem_count+1):
            sgpa = request.form.get(f"sgpa{i}")
            try:
                sgpas.append(float(sgpa))
            except:
                return f"<h3> Invalid SGPA entered</h3>"
        
        if len(sgpas) == 0:
            return "<h2> Enter the SGPA of atleast one semester</h2>"
        
        cgpa = sum(sgpas)/len(sgpas)
        return f"<h2 style='text-align:center;'>🎓 Your CGPA is: <b> {round(cgpa,2)}</b> </h2>"
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)


