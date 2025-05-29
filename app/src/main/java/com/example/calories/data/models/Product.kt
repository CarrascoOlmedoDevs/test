def generate_kotlin_data_classes():
    """Generates the Kotlin code string for Product and NutritionInfo data classes."""
    kotlin_code = """
package com.your_app_name.data.models

import kotlin.collections.List

data class NutritionInfo(
    val nutrientName: String,
    val value: Double,
    val unit: String
)

data class Product(
    val id: String?, // Optional ID, could also be Int? depending on use case
    val name: String,
    val barcode: String,
    val nutritionInfoList: List<NutritionInfo>
)
"""
    return kotlin_code.strip()

if __name__ == "__main__":
    # This part executes when the script is run directly.
    # It prints the generated Kotlin code to standard output.
    print(generate_kotlin_data_classes())