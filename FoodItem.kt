package com.yourproject.data.model

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class NutritionalInfo(
    val productName: String,
    val barcode: String?,
    val servingSize: String?,
    val servingSizeUnit: String?,
    val calories: Double?, // in kcal
    val fatTotal: Double?, // in g
    val fatSaturated: Double?, // in g
    val fatTrans: Double?, // in g
    val cholesterol: Double?, // in mg
    val sodium: Double?, // in mg
    val carbohydratesTotal: Double?, // in g
    val carbohydratesFiber: Double?, // in g
    val carbohydratesSugars: Double?, // in g
    val addedSugars: Double?, // in g
    val protein: Double?, // in g
    val vitaminD: Double?, // Units vary (mcg, IU) - need clarification or separate field
    val calcium: Double?, // in mg
    val iron: Double?, // in mg
    val potassium: Double?, // in mg
    val vitaminA: Double?, // Units vary (mcg RAE, IU)
    val vitaminC: Double? // in mg
    // Add more fields as needed for specific nutrients or micronutrients
    // val percentDailyValue: Map<String, Double>? // Optional: map of nutrient name to %DV
)