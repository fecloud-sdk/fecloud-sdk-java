package com.fecloud.sdk.core.exception;

import com.fecloud.sdk.core.http.HttpRequest;
import com.fecloud.sdk.core.http.HttpResponse;

public interface ExceptionHandler {
    void handleException(HttpRequest httpRequest, HttpResponse httpResponse) throws ServiceResponseException;
}
