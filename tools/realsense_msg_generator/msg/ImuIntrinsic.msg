# Motion device intrinsics: scale, bias, and variances

# Interpret data array values
                            # [ Scale X       cross axis        cross axis      Bias X]
                            # [cross axis      Scale Y          cross axis      Bias Y]
                            # [cross axis     cross axis          Scale Z       Bias Z]
float32[12] data            # 3x4 Row-major matrix

float32[3] noise_variances  # Variance of noise for X, Y, and Z axis
float32[3] bias_variances   # Variance of bias for X, Y, and Z axis