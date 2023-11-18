package com.fecloud.sdk.kms.v2.model;

import com.fecloud.sdk.core.SdkResponse;

import java.util.Objects;

/**
 * Response Object
 */
public class DisableKeyRotationResponse extends SdkResponse {

    @Override
    public boolean equals(java.lang.Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        return true;
    }

    @Override
    public int hashCode() {
        return Objects.hash();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class DisableKeyRotationResponse {\n");
        sb.append("}");
        return sb.toString();
    }

}
