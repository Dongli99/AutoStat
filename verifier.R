x <- c(1,2,3,4)
y <- c(2,4,4,6)

# Perform linear regression
model <- lm(y ~ x)

# Get regression coefficients
coefficients <- coef(model)
intercept <- coefficients[1]
slope <- coefficients[2]

# Print regression equation
cat("Regression Equation: y = ", round(slope, 3), "x +", round(intercept, 3), "\n")

# Calculate correlation coefficient
correlation <- cor(x, y)

# Print correlation coefficient
cat("Correlation Coefficient:", correlation, "\n")