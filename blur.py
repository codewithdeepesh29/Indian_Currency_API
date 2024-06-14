import cv2


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


def test_blurry(imagepath):
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"

    if (fm > 100):
        text = "Blurry"
    # show the image
    # cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # cv2.imshow("Image", image)
    # key = cv2.waitKey(0)
    return {"text": text, "fm": fm}
