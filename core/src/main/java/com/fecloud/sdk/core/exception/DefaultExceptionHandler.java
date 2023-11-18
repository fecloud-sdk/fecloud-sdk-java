package com.fecloud.sdk.core.exception;

import com.fecloud.sdk.core.Constants;
import com.fecloud.sdk.core.http.HttpRequest;
import com.fecloud.sdk.core.http.HttpResponse;
import com.fecloud.sdk.core.utils.ExceptionUtils;

public class DefaultExceptionHandler implements ExceptionHandler {
    @Override
    public void handleException(HttpRequest httpRequest, HttpResponse httpResponse) {
        if (httpResponse.getStatusCode() >= Constants.StatusCode.CLIENT_ERROR) {
            throw ServiceResponseException.mapException(httpResponse.getStatusCode(),
                    ExceptionUtils.extractErrorMessage(httpResponse));
        }
    }
}
