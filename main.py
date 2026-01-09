from log_file import setup_logging

# Import modules
import datacleaning
import feature_encoding
import visualisation

# Setup logging
logger = setup_logging("main")


def main():
    try:
        logger.info("===== TELCO CHURN PROJECT PIPELINE STARTED =====")

        # =========================
        # Step 1: Data Cleaning
        # =========================
        logger.info("Running Data Cleaning Module")
        datacleaning.main()
        logger.info("Data Cleaning Completed Successfully")

        # =========================
        # Step 2: Feature Encoding
        # =========================
        logger.info("Running Feature Encoding Module")
        feature_encoding.main()
        logger.info("Feature Encoding Completed Successfully")

        # =========================
        # Step 3: Visualisation
        # =========================
        logger.info("Running Visualisation Module")
        visualisation.main()
        logger.info("Visualisation Completed Successfully")

        logger.info("===== TELCO CHURN PROJECT PIPELINE FINISHED =====")

    except Exception as e:
        logger.error(f"Pipeline failed due to error: {e}")


if __name__ == "__main__":
    main()
