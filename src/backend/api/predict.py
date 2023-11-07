from fastapi import APIRouter, UploadFile
from utils.tensor import Tensor

router = APIRouter(prefix="/api/v1", tags=["/api/v1"])


@router.post("/predict")
def predict(image: UploadFile):
    tensor = Tensor(image.file.read())
    result = tensor.predict_image()
    return {"result": result}
