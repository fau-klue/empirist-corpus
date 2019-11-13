<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="no"/>
  
  <xsl:template match="/">
    <xsl:element name="corpus"><xsl:text>
</xsl:text>
    <xsl:copy-of select="corpus/text[@set='test' and @subcorpus='web']"></xsl:copy-of>
    <xsl:text>
</xsl:text>
    </xsl:element>
  </xsl:template>

</xsl:stylesheet>
