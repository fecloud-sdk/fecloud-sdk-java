package com.fecloud.sdk.kms.v2.region;

import com.fecloud.sdk.core.region.IRegionProvider;
import com.fecloud.sdk.core.region.Region;
import com.fecloud.sdk.core.region.RegionProviderChain;
import com.fecloud.sdk.core.utils.StringUtils;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class KmsRegion {

    public static final Region EU_WEST_0 =
        new Region("eu-west-0", "https://kms.eu-west-0.prod-cloud-ocb.orange-business.com");

    private static final IRegionProvider PROVIDER = RegionProviderChain.getDefaultRegionProviderChain("KMS");

    private static final Map<String, Region> STATIC_FIELDS = createStaticFields();

    private static Map<String, Region> createStaticFields() {
        Map<String, Region> map = new HashMap<>();
        map.put("eu-west-0", EU_WEST_0);
        return Collections.unmodifiableMap(map);
    }

    public static Region valueOf(String regionId) {
        if (StringUtils.isEmpty(regionId)) {
            throw new IllegalArgumentException("Unexpected empty parameter: regionId.");
        }

        Region result = PROVIDER.getRegion(regionId);
        if (Objects.nonNull(result)) {
            return result;
        }

        result = STATIC_FIELDS.get(regionId);
        if (Objects.nonNull(result)) {
            return result;
        }
        throw new IllegalArgumentException("Unexpected regionId: " + regionId);
    }
}
