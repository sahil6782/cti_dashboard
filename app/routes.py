from flask import Blueprint, render_template, request, current_app
from .api_client import check_virustotal, check_abuseipdb
from .database import save_ioc, get_recent_iocs
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def dashboard():
    iocs = get_recent_iocs(current_app.mongo)
    return render_template("dashboard.html", iocs=iocs)

@main.route("/lookup", methods=["POST"])
def lookup():
    ioc = request.form.get("ioc")
    result = {}
    if ioc:
        if ioc.replace(".", "").isdigit():
            result = check_abuseipdb(ioc)
        else:
            result = check_virustotal(ioc)
        result["ioc"] = ioc
        result["date"] = datetime.utcnow()
        save_ioc(current_app.mongo, result)

        if '_id' in result:
            del result['_id']

        return render_template("result.html", result=result)
