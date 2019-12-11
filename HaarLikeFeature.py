def enum(**enums):
    return type('Enum', (), enums)


FeatureType = enum(TWO_HORIZONTAL=(
    2, 1), THREE_HORIZONTAL=(3, 1), TWO_VERTICAL=(1, 2), THREE_VERTICAL=(1, 3), FOUR=(2, 2))
FeatureTypes = [FeatureType.TWO_VERTICAL, FeatureType.TWO_HORIZONTAL,
                FeatureType.THREE_VERTICAL, FeatureType.THREE_HORIZONTAL, FeatureType.FOUR]


class HaarLikeFeature(object):
    def __init__(self, featureType, topLeft, width, height, threshold, polarity):
        self.featureType = featureType
        self.topLeft = topLeft
        self.width = width
        self.height = height
        self.threshold = threshold
        self.polarity = polarity
        self.bottomRight = (topLeft[0] + width, topLeft[1] + height)
        self.weight = 1
