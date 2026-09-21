# Weights
def lightship_weight(structural, propulsion, outfit, margin):
    return structural + propulsion + outfit + margin


def structural_weight(block_coefficient, length_bp, breadth, depth, draft, K=0.032):
    cb_factor = block_coefficient + (1 - block_coefficient) * (0.8 * depth - draft) / (
        3 * draft
    )
    E = length_bp * (breadth + draft) + 0.85 * length_bp * (depth - draft) + 0.85 * 15
    return K * E**1.36 * (1 + (cb_factor - 0.7) / 2)


def propulsion_weight(maximum_continuous_rating):
    return 0.72 * maximum_continuous_rating**0.78


def outfit_weight(length_bp, breadth, Co=0.27):
    return Co * length_bp * breadth


def fuel_weight(maximum_continuous_rating, range, speed, SFR=0.00019, margin=0.05):
    return SFR * maximum_continuous_rating * range / speed * margin


def fresh_water_and_provisions_weight(crew, days):
    return 0.18 * crew * days


def crew_weight(crew):
    return 0.17 * crew


def total_deadweight(cargo_DWT, fuel, fresh_water_and_provisions, crew, lub=20):
    return cargo_DWT + fuel + lub + fresh_water_and_provisions + crew


# Centers
def vertical_center_of_gravity_hull(length_bp, depth, block_coefficient):
    return (
        0.01
        * depth
        * (46.6 + 0.135 * (0.81 - block_coefficient) * (length_bp / depth) ** 2)
    )


def longitudinal_center_of_gravity_hull(longitudinal_center_of_gravity):
    return -0.15 + longitudinal_center_of_gravity


def vertical_center_of_gravity_machinery(
    length_bp, breadth, draft, height_of_the_overhead_of_the_engine
):
    h_db = max(32 * breadth + 190 * draft ** (1 / 2), 45.7 + 0.417 * length_bp)
    return h_db + 0.35 * (height_of_the_overhead_of_the_engine - h_db)


def vertical_center_of_gravity_outfit(length_bp, depth):
    return depth + 1.25 + 0.01 * (length_bp - 125)


def longitudinal_center_of_gravity_machinery(length_bp, breadth, draft):
    return 0.5 * length_bp + 0.1 * (breadth - draft)


def KG_design(VCG, free_surface_margin, KG_margin=0.048):
    return VCG * (1 + free_surface_margin / 100) + KG_margin


def trim(LCG, LCB, length_bp, GM_long):
    return (LCG - LCB) * length_bp / GM_long
