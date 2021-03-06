# Read the blog (Japanese) to figure out how to use this script.
# https://gri-blog.hatenablog.com/entry/2019/12/09/162019
import forecastflow
from forecastflow.tabpy_support import make_prediction_schema
import datetime

# ============================================================================
# [Required] Fill your ForecastFlow parameters
email = "name@example.com"
password = "password"
project_id = "projectid"
model_id = "modelid"
# ============================================================================

# ============================================================================
# [Optional] Change display names
data_name = "Tableau Prep Data " + str(datetime.datetime.now())
prediction_name = "Tableau Prep Prediction " + str(datetime.datetime.now())
# ============================================================================

user = forecastflow.User(email, password)
get_output_schema = make_prediction_schema(user, project_id, model_id)


def ff_predict(input_data):
    project = user.get_project(project_id)
    model = project.get_model(model_id)
    prediction_data = project.create_data_source(
        input_data,
        data_name,
        forecastflow.DataSourceLabel.PREDICTION
    )
    prediction = model.create_prediction(
        prediction_data,
        prediction_name
    )
    result = prediction.get_result()
    return result
